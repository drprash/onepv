---
name: clinical-2x2-study-analyzer
description: Extracts binary outcome data from raw clinical study text,
  reconstructs 2x2 contingency tables, and produces publication-ready
  epidemiological risk analysis including RR, OR, ARR, NNT, confidence
  intervals, and statistical tests.
---

# Clinical Study 2×2 Outcome Analyzer

## Purpose

Analyze clinical research text describing binary outcomes and
automatically:

1.  Extract treatment and control group outcome data
2.  Construct a 2×2 contingency table
3.  Perform epidemiological risk calculations
4.  Conduct statistical significance testing
5.  Produce publication-ready results suitable for manuscripts

------------------------------------------------------------------------

# Capabilities

✔ Parse raw study text\
✔ Detect treatment and control arms\
✔ Extract event and non-event counts\
✔ Construct contingency tables\
✔ Calculate clinical effect measures\
✔ Compute confidence intervals\
✔ Run hypothesis tests\
✔ Produce publication-quality summaries

------------------------------------------------------------------------

# Input

Accept raw clinical study text.

Example:

In a randomized trial of 400 patients, 200 received Drug A and 200
received placebo. In the Drug A group, 45 patients experienced the
primary outcome while 155 did not. In the placebo group, 60 patients
experienced the outcome and 140 did not.

Alternate formats:

Drug A: 45/200 events\
Placebo: 60/200 events

Treatment group had 12 deaths out of 100 patients compared to 20 deaths
among 100 controls.

------------------------------------------------------------------------

# Step 1 --- Information Extraction

Detect treatment and control arms using keywords.

Treatment indicators: treatment, intervention, drug, exposed,
experimental

Control indicators: control, placebo, standard care, unexposed

Extract:

events_treatment\
total_treatment\
events_control\
total_control

Show the extracted numbers to the user and confirm the arm labels
before calculating. If the text is ambiguous (e.g. percentages without
denominators), ask rather than guess.

------------------------------------------------------------------------

# Calculation Script (use whenever code execution is available)

Run the bundled script with the extracted counts instead of calculating
by hand. It performs Steps 2--7 and 11 exactly (RR, OR, RD with 95% CIs,
ARR, RRR, NNT/NNH with CI, Pearson and Yates chi-square, two-sided
Fisher exact, Haldane--Anscombe correction, meta-analysis inputs):

    python3 scripts/analyze_2x2.py --events-treatment 45 --total-treatment 200 \
      --events-control 60 --total-control 200 \
      --treatment-label "Drug A" --control-label "Placebo"

Add `--json` for raw values. Use the script's numbers verbatim in the
report; write Steps 9--10 (manuscript summary, interpretation) from
them. If code execution is unavailable, compute manually using the
formulas below and say that results were calculated without code.

------------------------------------------------------------------------

# Step 2 --- Reconstruct 2×2 Table

              Event   No Event
  ----------- ------- ----------
  Treatment   a       b
  Control     c       d

Where:

a = events_treatment\
b = total_treatment − events_treatment\
c = events_control\
d = total_control − events_control

Apply Haldane--Anscombe correction if any cell is zero.

------------------------------------------------------------------------

# Step 3 --- Event Rates

Experimental Event Rate

EER = a / (a + b)

Control Event Rate

CER = c / (c + d)

------------------------------------------------------------------------

# Step 4 --- Effect Measures

Relative Risk

RR = EER / CER

Odds Ratio

OR = (a \* d) / (b \* c)

Risk Difference

RD = EER − CER

Absolute Risk Reduction

ARR = CER − EER

Relative Risk Reduction

RRR = ARR / CER

------------------------------------------------------------------------

# Step 5 --- Clinical Impact

Number Needed to Treat

NNT = 1 / ARR

Round upward.

Number Needed to Harm

NNH = 1 / ARI (ARI = EER − CER, when treatment increases risk)

------------------------------------------------------------------------

# Step 6 --- Confidence Intervals

Relative Risk

SE = sqrt((1/a) − (1/(a+b)) + (1/c) − (1/(c+d)))

lower = exp( ln(RR) − 1.96 \* SE ) upper = exp( ln(RR) + 1.96 \* SE )

Odds Ratio

SE = sqrt(1/a + 1/b + 1/c + 1/d)

lower = exp( ln(OR) − 1.96 \* SE ) upper = exp( ln(OR) + 1.96 \* SE )

------------------------------------------------------------------------

# Step 7 --- Statistical Tests

Chi-square test

χ² = Σ (observed − expected)² / expected

Fisher exact test for small samples.

------------------------------------------------------------------------

# Step 8 --- Publication Table

  Group       Event   No Event   Total   Event Rate
  ----------- ------- ---------- ------- ------------
  Treatment   a       b          a+b     EER
  Control     c       d          c+d     CER

------------------------------------------------------------------------

# Step 9 --- Manuscript Results

Report:

Relative Risk (95% CI)\
Odds Ratio (95% CI)\
Absolute Risk Reduction\
Relative Risk Reduction\
Number Needed to Treat

------------------------------------------------------------------------

# Step 10 --- Interpretation

Provide neutral academic interpretation describing effect size,
direction, and statistical significance.

------------------------------------------------------------------------

# Step 11 --- Meta-analysis Output

treatment_events\
treatment_total\
control_events\
control_total\
RR\
logRR\
SE_logRR

------------------------------------------------------------------------

# Output Order

1.  Extracted data
2.  Contingency table
3.  Event rates
4.  Effect measures
5.  Confidence intervals
6.  Hypothesis tests
7.  Publication-ready table
8.  Manuscript-ready summary

------------------------------------------------------------------------

# Quality Guidelines

Use precise calculations internally.\
Round to 2--3 decimals for reporting.\
Prefer Fisher test when expected counts are small.\
Always present absolute and relative risks together.
