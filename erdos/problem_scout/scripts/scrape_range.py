from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from pathlib import Path

import requests
import yaml


TAG_RE = re.compile(r"<[^>]+>")
BOX_RE = re.compile(r'<div class="problem-box">(?P<body>.*?)(?=<div class="container">\s*<div class="problem-box">|</body>)', re.S)


def clean(raw: str) -> str:
    raw = raw.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    raw = re.sub(r"</p\s*>", "\n", raw, flags=re.I)
    raw = re.sub(r"</div\s*>", "\n", raw, flags=re.I)
    text = TAG_RE.sub("", raw)
    text = html.unescape(text)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def first_group(pattern: str, text: str, default: str = "") -> str:
    m = re.search(pattern, text, re.S)
    return html.unescape(m.group(1)).strip() if m else default


def parse_box(box: str) -> dict | None:
    number = first_group(r'<div id="problem_id">.*?<a href="/([0-9-]+)">', box)
    if not number:
        return None

    content = clean(first_group(r'<div id="content">(.*?)</div>', box))
    additional = clean(first_group(r'<div class="problem-additional-text">(.*?)</div>\s*</div>', box))
    official_state = first_group(r'<div class="problem-text" id="([^"]+)"', box)
    activity_state = first_group(r'data-current-status="([^"]+)"', box)
    activity_description = first_group(
        r'data-status="' + re.escape(activity_state) + r'".*?data-description="([^"]+)"',
        box,
    ) if activity_state else ""
    comments_raw = first_group(r'([0-9]+)\s+comments?\s+on this problem', box, "0")
    tags = sorted(set(html.unescape(t).replace("%20", " ") for t in re.findall(r'/tags/([^"]+)"', box)))
    prize = clean(first_group(r'<div id="prize">(.*?)</div>', box))
    prize = prize.replace("\n", " ")

    return {
        "number": number,
        "url": f"https://www.erdosproblems.com/{number}",
        "official_state_page": official_state,
        "activity_state": activity_state,
        "activity_description": clean(activity_description),
        "comments": int(comments_raw),
        "prize_page": prize,
        "tags_page": tags,
        "statement": content,
        "additional_text": additional,
    }


def fetch_range(url: str, cache: Path, refresh: bool) -> str:
    if cache.exists() and not refresh:
        return cache.read_text(encoding="utf-8")
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    cache.write_text(response.text, encoding="utf-8")
    return response.text


def load_yaml_metadata(path: Path) -> dict[str, dict]:
    items = yaml.safe_load(path.read_text(encoding="utf-8"))
    return {str(item["number"]): item for item in items}


def merge(yaml_meta: dict[str, dict], range_meta: dict[str, dict]) -> list[dict]:
    out = []
    for number, base in sorted(yaml_meta.items(), key=lambda kv: int(kv[0].split("-")[0])):
        row = {
            "number": number,
            "url": f"https://www.erdosproblems.com/{number}",
            "status": base.get("status", {}).get("state", ""),
            "status_last_update": base.get("status", {}).get("last_update", ""),
            "prize": base.get("prize", ""),
            "formalized": base.get("formalized", {}).get("state", ""),
            "formalized_last_update": base.get("formalized", {}).get("last_update", ""),
            "tags": base.get("tags", []),
            "oeis": base.get("oeis", []),
            "comments_yaml": base.get("comments", ""),
        }
        row.update(range_meta.get(number, {}))
        if not row.get("statement"):
            row["statement"] = ""
        if not row.get("comments"):
            row["comments"] = 0
        if not row.get("activity_state"):
            row["activity_state"] = ""
        out.append(row)
    return out


GOOD_TAGS = {
    "covering systems",
    "divisors",
    "factorials",
    "diophantine equations",
    "graphs",
    "graph theory",
    "computational",
    "sets",
    "probability",
}

HARD_TAGS = {
    "primes",
    "additive combinatorics",
    "arithmetic progressions",
    "ramsey theory",
    "sieve theory",
}


def prize_value(prize: str) -> int:
    m = re.search(r"\$([0-9,]+)", prize or "")
    return int(m.group(1).replace(",", "")) if m else 0


def heuristic_score(row: dict) -> int:
    score = 45
    status = row.get("status", "")
    if status in {"verifiable", "falsifiable", "decidable"}:
        score += 25
    elif status != "open":
        score -= 40
    if row.get("formalized") == "yes":
        score += 6
    tags = set(row.get("tags") or [])
    score += 4 * len(tags & GOOD_TAGS)
    score -= 4 * len(tags & HARD_TAGS)
    comments = int(row.get("comments") or 0)
    if comments == 0:
        score += 7
    elif comments <= 2:
        score += 4
    elif comments >= 8:
        score -= 4
    if row.get("activity_state") == "partial":
        score += 8
    elif row.get("activity_state") == "solution":
        score -= 8
    pv = prize_value(row.get("prize") or row.get("prize_page") or "")
    if pv >= 5000:
        score -= 12
    elif pv >= 1000:
        score -= 7
    elif pv > 0:
        score -= 3
    st = row.get("statement", "")
    if st:
        if len(st) < 250:
            score += 5
        elif len(st) > 1000:
            score -= 5
    return max(0, min(100, score))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--range-url", default="https://www.erdosproblems.com/range/1-1217")
    args = parser.parse_args()

    repo = args.root / "erdosproblems"
    scout = args.root / "erdos" / "problem_scout"
    data_dir = scout / "data"
    report_dir = scout / "reports"
    data_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    yaml_meta = load_yaml_metadata(repo / "data" / "problems.yaml")
    html_text = fetch_range(args.range_url, data_dir / "range_1_1217.html", args.refresh)
    boxes = [parse_box(m.group("body")) for m in BOX_RE.finditer(html_text)]
    range_meta = {b["number"]: b for b in boxes if b}
    rows = merge(yaml_meta, range_meta)
    for row in rows:
        row["heuristic_score"] = heuristic_score(row)

    json_path = data_dir / "problem_metadata.jsonl"
    with json_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    csv_path = data_dir / "problem_metadata.csv"
    fields = [
        "number",
        "status",
        "heuristic_score",
        "comments",
        "activity_state",
        "formalized",
        "prize",
        "tags",
        "url",
        "statement",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})

    candidates = [
        r
        for r in rows
        if r.get("status") in {"open", "verifiable", "falsifiable", "decidable"}
    ]
    candidates.sort(key=lambda r: (r["heuristic_score"], -int(r.get("comments") or 0)), reverse=True)

    md = []
    md.append("# Erdős Problems All-Site Metadata Scout\n")
    md.append(f"- Source range page: {args.range_url}\n")
    md.append(f"- Parsed problems from YAML: {len(rows)}\n")
    md.append(f"- Parsed problem boxes from range page: {len(range_meta)}\n")
    md.append(f"- Candidate states considered: open, verifiable, falsifiable, decidable\n")
    md.append("\n## Top Heuristic Candidates\n")
    md.append("| # | score | status | comments | activity | tags | statement preview |\n")
    md.append("|---:|---:|---|---:|---|---|---|\n")
    for r in candidates[:80]:
        preview = (r.get("statement") or "").replace("\n", " ")
        preview = preview[:220] + ("..." if len(preview) > 220 else "")
        tags = ", ".join(r.get("tags") or [])
        md.append(
            f"| [{r['number']}]({r['url']}) | {r['heuristic_score']} | {r.get('status','')} | "
            f"{r.get('comments',0)} | {r.get('activity_state','')} | {tags} | {preview} |\n"
        )
    (report_dir / "metadata_top80.md").write_text("".join(md), encoding="utf-8")

    print(f"wrote {json_path}")
    print(f"wrote {csv_path}")
    print(f"wrote {report_dir / 'metadata_top80.md'}")
    print(f"rows={len(rows)} boxes={len(range_meta)} candidates={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
