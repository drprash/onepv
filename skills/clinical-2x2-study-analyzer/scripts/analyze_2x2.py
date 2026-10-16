#!/usr/bin/env python3
"""Exact 2x2 outcome analysis for the clinical-2x2-study-analyzer skill.

Standard library only, so it runs in any Python 3.8+ sandbox.

Usage:
  python3 analyze_2x2.py --events-treatment 45 --total-treatment 200 \
                         --events-control 60 --total-control 200 \
                         [--treatment-label "Drug A"] [--control-label "Placebo"] [--json]
"""
import argparse
import json
import math
import sys
from statistics import NormalDist

Z = NormalDist().inv_cdf(0.975)  # 1.959964...


def chi_square(a, b, c, d, yates=False):
    n = a + b + c + d
    rows, cols = (a + b, c + d), (a + c, b + d)
    observed = ((a, b), (c, d))
    stat, min_expected = 0.0, float("inf")
    for i in range(2):
        for j in range(2):
            e = rows[i] * cols[j] / n
            min_expected = min(min_expected, e)
            diff = abs(observed[i][j] - e)
            if yates:
                diff = max(0.0, diff - 0.5)
            stat += diff * diff / e if e else 0.0
    p = math.erfc(math.sqrt(stat / 2))  # chi-square survival function, df = 1
    return stat, p, min_expected


def fisher_exact(a, b, c, d):
    """Two-sided Fisher exact p-value (sum of tables as or less probable)."""
    r1, r2, c1 = a + b, c + d, a + c
    n = r1 + r2

    def log_p(x):
        return (math.lgamma(r1 + 1) - math.lgamma(x + 1) - math.lgamma(r1 - x + 1)
                + math.lgamma(r2 + 1) - math.lgamma(c1 - x + 1) - math.lgamma(r2 - c1 + x + 1)
                - math.lgamma(n + 1) + math.lgamma(c1 + 1) + math.lgamma(n - c1 + 1))

    observed = log_p(a)
    lo, hi = max(0, c1 - r2), min(r1, c1)
    p = sum(math.exp(log_p(x)) for x in range(lo, hi + 1) if log_p(x) <= observed + 1e-7)
    return min(1.0, p)


def nnt_label(rd):
    """Number needed to treat (benefit) or harm, rounded up, from RD = EER - CER."""
    if rd == 0:
        return "infinite (no difference)"
    n = math.ceil(1 / abs(rd))
    return f"NNT (benefit) = {n}" if rd < 0 else f"NNH (harm) = {n}"


def nnt_ci_label(rd_lo, rd_hi):
    """Altman's method: invert the RD confidence interval."""
    def side(x):
        return f"{'NNTB' if x < 0 else 'NNTH'} {abs(1 / x):.1f}"
    if rd_lo == 0 or rd_hi == 0:
        return "not estimable (CI limit at zero)"
    if (rd_lo < 0) == (rd_hi < 0):
        a, b = sorted((abs(1 / rd_lo), abs(1 / rd_hi)))
        return f"{'NNTB' if rd_lo < 0 else 'NNTH'} {a:.1f} to {b:.1f}"
    return f"{side(rd_lo)} to infinity to {side(rd_hi)} (CI includes no effect)"


def analyze(et, nt, ec, nc):
    a, b, c, d = et, nt - et, ec, nc - ec
    corrected = 0 in (a, b, c, d)
    ca, cb, cc, cd = (x + 0.5 for x in (a, b, c, d)) if corrected else (a, b, c, d)

    eer, cer = a / nt, c / nc
    rd = eer - cer
    rd_se = math.sqrt(eer * (1 - eer) / nt + cer * (1 - cer) / nc)
    rd_lo, rd_hi = rd - Z * rd_se, rd + Z * rd_se

    rr = (ca / (ca + cb)) / (cc / (cc + cd))
    rr_se = math.sqrt(1 / ca - 1 / (ca + cb) + 1 / cc - 1 / (cc + cd))
    or_ = (ca * cd) / (cb * cc)
    or_se = math.sqrt(1 / ca + 1 / cb + 1 / cc + 1 / cd)

    chi2, chi2_p, min_exp = chi_square(a, b, c, d)
    chi2_y, chi2_y_p, _ = chi_square(a, b, c, d, yates=True)
    fisher_p = fisher_exact(a, b, c, d)
    use_fisher = min_exp < 5

    return {
        "table": {"a": a, "b": b, "c": c, "d": d, "n": nt + nc},
        "haldane_anscombe_correction_applied": corrected,
        "event_rates": {"EER": eer, "CER": cer},
        "relative_risk": {"RR": rr, "ci95": [math.exp(math.log(rr) - Z * rr_se), math.exp(math.log(rr) + Z * rr_se)]},
        "odds_ratio": {"OR": or_, "ci95": [math.exp(math.log(or_) - Z * or_se), math.exp(math.log(or_) + Z * or_se)]},
        "risk_difference": {"RD": rd, "ci95": [rd_lo, rd_hi]},
        "ARR": cer - eer,
        "RRR": (cer - eer) / cer if cer else None,
        "NNT": nnt_label(rd),
        "NNT_ci95": nnt_ci_label(rd_lo, rd_hi),
        "tests": {
            "chi_square": {"statistic": chi2, "p": chi2_p},
            "chi_square_yates": {"statistic": chi2_y, "p": chi2_y_p},
            "fisher_exact": {"p": fisher_p},
            "min_expected_count": min_exp,
            "recommended": "fisher_exact" if use_fisher else "chi_square",
        },
        "meta_analysis": {
            "treatment_events": et, "treatment_total": nt,
            "control_events": ec, "control_total": nc,
            "RR": rr, "logRR": math.log(rr), "SE_logRR": rr_se,
        },
    }


def fmt_p(p):
    return "< 0.001" if p < 0.001 else f"{p:.3f}"


def markdown(r, tl, cl):
    t, er = r["table"], r["event_rates"]
    rr, or_, rd = r["relative_risk"], r["odds_ratio"], r["risk_difference"]
    tests = r["tests"]
    rec = tests["recommended"]
    rec_p = tests[rec]["p"]
    lines = [
        "| Group | Event | No Event | Total | Event Rate |",
        "|-------|-------|----------|-------|------------|",
        f"| {tl} | {t['a']} | {t['b']} | {t['a'] + t['b']} | {er['EER']:.1%} |",
        f"| {cl} | {t['c']} | {t['d']} | {t['c'] + t['d']} | {er['CER']:.1%} |",
        "",
        "| Measure | Estimate | 95% CI |",
        "|---------|----------|--------|",
        f"| Relative risk | {rr['RR']:.3f} | {rr['ci95'][0]:.3f} to {rr['ci95'][1]:.3f} |",
        f"| Odds ratio | {or_['OR']:.3f} | {or_['ci95'][0]:.3f} to {or_['ci95'][1]:.3f} |",
        f"| Risk difference (EER − CER) | {rd['RD']:.3f} | {rd['ci95'][0]:.3f} to {rd['ci95'][1]:.3f} |",
        f"| Absolute risk reduction | {r['ARR']:.3f} | |",
        f"| Relative risk reduction | {r['RRR']:.1%} | |" if r["RRR"] is not None else "| Relative risk reduction | not defined (CER = 0) | |",
        f"| Number needed to treat / harm | {r['NNT']} | {r['NNT_ci95']} |",
        "",
        "| Test | Statistic | p-value |",
        "|------|-----------|---------|",
        f"| Pearson chi-square | {tests['chi_square']['statistic']:.3f} | {fmt_p(tests['chi_square']['p'])} |",
        f"| Chi-square (Yates) | {tests['chi_square_yates']['statistic']:.3f} | {fmt_p(tests['chi_square_yates']['p'])} |",
        f"| Fisher exact (two-sided) | | {fmt_p(tests['fisher_exact']['p'])} |",
        "",
        f"Recommended test: **{rec.replace('_', '-' if rec == 'chi_square' else ' ')}** (minimum expected count {tests['min_expected_count']:.1f}); "
        f"p = {fmt_p(rec_p)}, {'statistically significant' if rec_p < 0.05 else 'not statistically significant'} at α = 0.05.",
    ]
    if r["haldane_anscombe_correction_applied"]:
        lines.append("Note: a zero cell was present, so 0.5 was added to every cell for RR and OR (Haldane–Anscombe correction).")
    m = r["meta_analysis"]
    lines += ["", f"Meta-analysis inputs: logRR = {m['logRR']:.4f}, SE(logRR) = {m['SE_logRR']:.4f}"]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--events-treatment", type=int, required=True)
    p.add_argument("--total-treatment", type=int, required=True)
    p.add_argument("--events-control", type=int, required=True)
    p.add_argument("--total-control", type=int, required=True)
    p.add_argument("--treatment-label", default="Treatment")
    p.add_argument("--control-label", default="Control")
    p.add_argument("--json", action="store_true", help="print raw results as JSON")
    args = p.parse_args()

    et, nt, ec, nc = args.events_treatment, args.total_treatment, args.events_control, args.total_control
    if min(et, ec) < 0 or nt <= 0 or nc <= 0 or et > nt or ec > nc:
        sys.exit("Error: counts must satisfy 0 <= events <= total and total > 0 in each group.")
    if et + ec == 0 or et + ec == nt + nc:
        sys.exit("Error: no variation in outcome (all or no participants had the event); effect measures are undefined.")

    result = analyze(et, nt, ec, nc)
    print(json.dumps(result, indent=2) if args.json else markdown(result, args.treatment_label, args.control_label))


if __name__ == "__main__":
    main()
