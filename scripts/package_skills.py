#!/usr/bin/env python3
"""Package each skill in skills/ as an upload-ready ZIP for claude.ai.

Each ZIP contains one top-level folder named after the skill, holding SKILL.md
and any supporting files (e.g. references/). Output goes to dist/<skill>.zip.

Usage: python3 scripts/package_skills.py
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}
# Fixed timestamp so rebuilding unchanged skills produces identical ZIPs
FIXED_DATE = (2020, 1, 1, 0, 0, 0)


def frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("missing YAML frontmatter")
    fields, key = {}, None
    for line in m.group(1).split("\n"):
        top = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if top:
            key = top.group(1)
            fields[key] = top.group(2).strip()
        elif key:
            fields[key] += " " + line.strip()
    return {k: " ".join(v.lstrip(">|").split()) for k, v in fields.items()}


def validate(skill_dir: Path) -> list:
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["SKILL.md not found"]
    try:
        fm = frontmatter(skill_md)
    except ValueError as e:
        return [str(e)]
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != skill_dir.name:
        errors.append(f"name '{name}' does not match folder '{skill_dir.name}'")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("name must be 1-64 lowercase letters, digits or hyphens")
    if not desc:
        errors.append("description is empty")
    elif len(desc) > 1024:
        errors.append(f"description is {len(desc)} characters (max 1024)")
    if re.search(r"[<>]", desc):
        errors.append("description contains '<' or '>'")
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        errors.append(f"unsupported frontmatter keys: {', '.join(sorted(extra))}")
    return errors


def package(skill_dir: Path) -> Path:
    out = DIST_DIR / f"{skill_dir.name}.zip"
    files = sorted(p for p in skill_dir.rglob("*")
                   if p.is_file() and p.name not in SKIP_NAMES
                   and not any(part.startswith(".") for part in p.relative_to(skill_dir).parts))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            arcname = f"{skill_dir.name}/{f.relative_to(skill_dir).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, f.read_bytes())
    return out


def main() -> int:
    DIST_DIR.mkdir(exist_ok=True)
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))
    failed = False
    for d in skill_dirs:
        errors = validate(d)
        if errors:
            failed = True
            print(f"FAIL  {d.name}")
            for e in errors:
                print(f"      - {e}")
            continue
        out = package(d)
        print(f"OK    {out.relative_to(ROOT)}  ({out.stat().st_size // 1024} KB)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
