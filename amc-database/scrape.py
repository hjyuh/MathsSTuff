"""AMC Problem Scraper — fetches problems + solutions from AoPS wiki."""

import requests
import re
import json
import time
import os
import sys

BASE_URL = "https://artofproblemsolving.com/wiki/index.php"
RAW_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "amc_raw.json")

DELAY = 2.0  # seconds between requests (be polite to avoid Cloudflare)

# All tests to scrape
TESTS = []
for _year in range(2015, 2026):
    # AMC 8 — cancelled in 2020
    if _year != 2020:
        TESTS.append({"year": _year, "test": "AMC 8", "slug": f"{_year}_AMC_8", "num_problems": 25})
    # AMC 10A/10B and 12A/12B
    for _variant in ["10A", "10B", "12A", "12B"]:
        TESTS.append({"year": _year, "test": f"AMC {_variant}", "slug": f"{_year}_AMC_{_variant}", "num_problems": 25})


def raw_url(page_title: str) -> str:
    """Build URL for raw wiki markup of a page."""
    return f"{BASE_URL}?title={page_title}&action=raw"


def fetch_page(page_title: str, depth: int = 0) -> str | None:
    """Fetch raw wiki markup for a page, following redirects. Returns None on failure."""
    if depth > 3:
        print(f"  [WARN] Too many redirects for {page_title}")
        return None
    url = raw_url(page_title)
    try:
        resp = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        })
        if resp.status_code == 200:
            text = resp.text
            # Detect Cloudflare block
            if "Attention Required" in text or "you have been blocked" in text:
                print(f"\n  [BLOCKED] Cloudflare blocked request for {page_title}")
                return None
            # Handle wiki redirects: #redirect[[Page Title]] or #REDIRECT[[Page_Title]]
            redir = re.match(r'\s*#redirect\s*\[\[([^\]|]+)', text, re.IGNORECASE)
            if redir:
                target = redir.group(1).replace(" ", "_")
                if depth == 0:
                    print(f"(redirect->{target})", end=" ", flush=True)
                time.sleep(DELAY)
                return fetch_page(target, depth + 1)
            return text
        print(f"  [WARN] HTTP {resp.status_code} for {page_title}")
        return None
    except requests.RequestException as e:
        print(f"  [ERROR] {e} for {page_title}")
        return None


def parse_answer_choices(text: str) -> dict:
    """Extract answer choices from a \\textbf{(A)} ... block."""
    choices = {}
    # Match \textbf{(X) } or \textbf{(X)} followed by content up to next choice or end
    pattern = r'\\textbf\{\(([A-E])\)\s*\}\s*(.*?)(?=\\textbf\{\([A-E]\)\s*\}|</imath>|$)'
    for m in re.finditer(pattern, text, re.DOTALL):
        letter = m.group(1)
        value = m.group(2).strip()
        # Clean up \qquad and trailing whitespace
        value = re.sub(r'\\qquad\s*', '', value).strip()
        choices[letter] = value
    return choices


def parse_problem_list(markup: str, slug: str) -> list[dict]:
    """Parse a problem list page into individual problem stubs."""
    problems = []
    # Split by ==Problem N== headers
    parts = re.split(r'==\s*Problem\s+(\d+)\s*==', markup)
    # parts[0] is preamble, then alternating: number, content, number, content...
    for i in range(1, len(parts) - 1, 2):
        num = int(parts[i])
        content = parts[i + 1].strip()

        # Remove the solution link line
        content = re.sub(r'\[\[.*?\|Solution\]\]', '', content).strip()

        # Try to split problem text from answer choices
        # Answer choices are in a <imath> or <math> block with \textbf{(A)}
        answer_match = re.search(
            r'(<(?:imath|math)>.*?\\textbf\{\(A\)\s*\}.*?</(?:imath|math)>)',
            content, re.DOTALL
        )

        if answer_match:
            choices_raw = answer_match.group(1)
            problem_text = content[:answer_match.start()].strip()
            choices = parse_answer_choices(choices_raw)
        else:
            problem_text = content
            choices = {}

        problems.append({
            "id": f"{slug}_P{num}",
            "number": num,
            "problem": problem_text,
            "choices": choices,
        })

    return problems


def parse_solution_page(markup: str) -> dict:
    """Parse an individual problem+solution page.

    Returns {"problem": str, "answer": str, "solutions": [str]}
    """
    result = {"problem": "", "answer": "", "solutions": []}

    # Extract problem section
    prob_match = re.search(r'==\s*Problem\s*==\s*(.*?)(?===)', markup, re.DOTALL)
    if prob_match:
        result["problem"] = prob_match.group(1).strip()

    # Extract answer from \boxed in any solution
    # Patterns seen in the wild:
    #   \boxed{\textbf{(E) } 64}       — most common
    #   \text{\boxed{\textbf{(E) }18}} — wrapped in \text
    #   \boxed{(E)}                    — simple parens
    #   \boxed{\text{(E)}}             — parens in \text
    #   \boxed{B}                      — bare letter
    #   \boxed{\textbf B}              — bold bare letter
    #   \boxed{\textbf{D}}             — bold letter in braces
    answer_patterns = [
        r'\\boxed\s*\{[^}]*\\textbf\{\(([A-E])\)',        # \boxed{...\textbf{(X)...}
        r'\\text\{\\boxed\s*\{\\textbf\{\(([A-E])\)',      # \text{\boxed{\textbf{(X)...}
        r'\\boxed\s*\{[^}]*\(\\textbf\s*\{?([A-E])\}?\)', # \boxed{...(\textbf{X})...} or \boxed{(\textbf X)}
        r'\\boxed\s*\{\\text\{\(\\textbf\s+([A-E])\)',     # \boxed{\text{(\textbf X)...}
        r'\\boxed\s*\{[^}]*\(([A-E])\)',                   # \boxed{...(X)...}
        r'\\boxed\s*\{\\text\{?\(([A-E])\)',               # \boxed{\text{(X)}
        r'\\boxed\s*\{\\text\{([A-E])\s',                  # \boxed{\text{X ...}
        r'\\boxed\s*\{\\textbf\s*\{([A-E])\}',             # \boxed{\textbf{X}}
        r'\\boxed\s*\{\\textbf\s+([A-E])\}',               # \boxed{\textbf X}
        r'\\boxed\s*\{([A-E])\}',                          # \boxed{X}
    ]
    for pat in answer_patterns:
        answer_match = re.search(pat, markup)
        if answer_match:
            result["answer"] = answer_match.group(1)
            break

    # Fallback: look for \textbf{ (X)} or \textbf{(X)} near end of solution text (no \boxed)
    if not result["answer"]:
        # Search in solution sections for "answer is ... \textbf{ (X)}" pattern
        fallback = re.search(r'answer\s+is\s+.*?\\textbf\{\s*\(([A-E])\)', markup, re.IGNORECASE)
        if not fallback:
            fallback = re.search(r'\\textbf\{\s*\(([A-E])\)\s*\}', markup)
        if not fallback:
            fallback = re.search(r'\\textbf\s*\{\s*([A-E])\s*\}', markup)
        if fallback:
            result["answer"] = fallback.group(1)

    # Extract solutions — split by ==Solution headers
    sol_parts = re.split(r'==+\s*Solution\s*\d*\s*(?:\([^)]*\))?\s*==+', markup)
    for part in sol_parts[1:]:
        # Stop at next major section
        cleaned = re.split(r'==+\s*(?:See [Aa]lso|Video|Note|Diagram)\s*', part, maxsplit=1)[0]
        cleaned = cleaned.strip()
        if cleaned and len(cleaned) > 20:
            # Remove user signatures at end of lines
            cleaned = re.sub(r'~+\s*\[?[^\]\n]*\]?\s*$', '', cleaned, flags=re.MULTILINE).strip()
            result["solutions"].append(cleaned)

    return result


def scrape_test(test_info: dict) -> list[dict]:
    """Scrape all problems + solutions for one test."""
    slug = test_info["slug"]
    test_name = test_info["test"]
    year = test_info["year"]

    print(f"\n{'='*60}")
    print(f"Scraping {year} {test_name} ({slug})")
    print(f"{'='*60}")

    # Fetch problem list page
    list_markup = fetch_page(f"{slug}_Problems")
    if not list_markup:
        print(f"  [SKIP] Could not fetch problem list for {slug}")
        return []

    time.sleep(DELAY)

    # Parse problem list for problem text + choices
    problem_stubs = parse_problem_list(list_markup, slug)
    print(f"  Found {len(problem_stubs)} problems on list page")

    results = []
    for stub in problem_stubs:
        num = stub["number"]
        print(f"  Problem {num}...", end=" ", flush=True)

        # Fetch individual solution page
        sol_markup = fetch_page(f"{slug}_Problems/Problem_{num}")
        time.sleep(DELAY)

        if sol_markup:
            sol_data = parse_solution_page(sol_markup)
            entry = {
                "id": f"{slug}_P{num}",
                "test": test_name,
                "year": year,
                "number": num,
                "problem": stub["problem"] if stub["problem"] else sol_data["problem"],
                "choices": stub["choices"],
                "answer": sol_data["answer"],
                "solutions": sol_data["solutions"],
            }
            print(f"OK (answer={sol_data['answer']}, {len(sol_data['solutions'])} solutions)")
        else:
            entry = {
                "id": f"{slug}_P{num}",
                "test": test_name,
                "year": year,
                "number": num,
                "problem": stub["problem"],
                "choices": stub["choices"],
                "answer": "",
                "solutions": [],
            }
            print("FAILED (no solution page)")

        results.append(entry)

    return results


def save_raw_text(test_slug: str, problems: list[dict]):
    """Save problems as a readable text file."""
    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, f"{test_slug}.txt")
    with open(path, "w", encoding="utf-8") as f:
        for p in problems:
            f.write(f"=== Problem {p['number']} ===\n")
            f.write(f"{p['problem']}\n\n")
            if p["choices"]:
                f.write(f"Choices: {p['choices']}\n")
            f.write(f"Answer: {p['answer']}\n\n")
            for i, sol in enumerate(p["solutions"], 1):
                f.write(f"--- Solution {i} ---\n{sol}\n\n")
            f.write("\n")
    print(f"  Saved {path}")


def fix_missing_answers():
    """Re-fetch only problems with missing answers and update the JSON."""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        all_problems = json.load(f)

    missing = [p for p in all_problems if not p["answer"]]
    print(f"Found {len(missing)} problems with missing answers")

    fixed = 0
    for p in missing:
        # Build the solution page title from the ID
        # ID format: 2023_AMC_10A_P18 -> 2023_AMC_10A_Problems/Problem_18
        parts = p["id"].rsplit("_P", 1)
        page_title = f"{parts[0]}_Problems/Problem_{parts[1]}"
        print(f"  {p['id']}...", end=" ", flush=True)

        markup = fetch_page(page_title)
        time.sleep(DELAY)

        if markup:
            sol_data = parse_solution_page(markup)
            if sol_data["answer"]:
                p["answer"] = sol_data["answer"]
                if not p["solutions"] and sol_data["solutions"]:
                    p["solutions"] = sol_data["solutions"]
                print(f"FIXED -> {sol_data['answer']}")
                fixed += 1
            else:
                print("still no answer")
        else:
            print("fetch failed")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_problems, f, indent=2, ensure_ascii=False)
    print(f"\nFixed {fixed}/{len(missing)} missing answers")


def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    # Allow filtering: python scrape.py 2023_AMC_10A
    # Or fix mode: python scrape.py --fix
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        fix_missing_answers()
        return

    all_problems = []
    failed_tests = []
    filter_slug = sys.argv[1] if len(sys.argv) > 1 else None

    for test_info in TESTS:
        if filter_slug and test_info["slug"] != filter_slug:
            continue

        problems = scrape_test(test_info)
        if problems:
            save_raw_text(test_info["slug"], problems)
            all_problems.extend(problems)
        else:
            failed_tests.append(test_info["slug"])

    # Save combined JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_problems, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(all_problems)} problems to {OUTPUT_FILE}")

    if failed_tests:
        print(f"\nFailed tests: {failed_tests}")

    print(f"\nDone! {len(all_problems)} problems scraped.")


if __name__ == "__main__":
    main()
