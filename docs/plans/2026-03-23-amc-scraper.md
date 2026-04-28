# AMC Problem Scraper Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Scrape all AMC 8/10A/10B/12A/12B problems and solutions (2015–2025) from AoPS wiki into structured JSON.

**Architecture:** Single Python script using `requests` to fetch raw wiki markup via MediaWiki `?action=raw` endpoint. Parse wiki markup with regex to extract problems, answer choices, and solutions. Output raw `.txt` files per test + one flat `amc_raw.json`.

**Tech Stack:** Python 3, `requests`, `re`, `json`, `time`

---

### Task 1: Project scaffold and test infrastructure

**Files:**
- Create: `amc-database/scrape.py`
- Create: `amc-database/test_scrape.py`

**Step 1: Create scrape.py with constants and URL builder**

```python
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

DELAY = 1.5  # seconds between requests

# All tests to scrape
TESTS = []
for year in range(2015, 2026):
    # AMC 8 — cancelled in 2020
    if year != 2020:
        TESTS.append({"year": year, "test": "AMC 8", "slug": f"{year}_AMC_8", "num_problems": 25})
    # AMC 10A/10B and 12A/12B
    for variant in ["10A", "10B", "12A", "12B"]:
        TESTS.append({"year": year, "test": f"AMC {variant}", "slug": f"{year}_AMC_{variant}", "num_problems": 25})


def raw_url(page_title: str) -> str:
    """Build URL for raw wiki markup of a page."""
    return f"{BASE_URL}?title={page_title}&action=raw"


def fetch_page(page_title: str) -> str | None:
    """Fetch raw wiki markup for a page. Returns None on failure."""
    url = raw_url(page_title)
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "AMCScraper/1.0 (educational)"})
        if resp.status_code == 200:
            return resp.text
        print(f"  [WARN] HTTP {resp.status_code} for {page_title}")
        return None
    except requests.RequestException as e:
        print(f"  [ERROR] {e} for {page_title}")
        return None
```

**Step 2: Verify constants are correct**

Run: `python -c "import sys; sys.path.insert(0, 'amc-database'); from scrape import TESTS; print(f'{len(TESTS)} tests'); print(TESTS[0]); print(TESTS[-1])"`

Expected: 54 tests (10 AMC8 + 44 AMC10/12), first is 2015 AMC 8, last is 2025 AMC 12B.

---

### Task 2: Parse problem list page

**Files:**
- Modify: `amc-database/scrape.py`

**Step 1: Add problem list parser**

```python
def parse_answer_choices(text: str) -> dict:
    """Extract answer choices from a \\textbf{(A)} ... block."""
    choices = {}
    # Match \textbf{(X) } or \textbf{(X)} followed by content
    pattern = r'\\textbf\{\(([A-E])\)\s*\}\s*([^\\]+?)(?=\\textbf\{\([A-E]\)\s*\}|$)'
    for m in re.finditer(pattern, text):
        letter = m.group(1)
        value = m.group(2).strip().rstrip('\\').strip()
        # Clean up \qquad and whitespace
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
        # Answer choices are in a <imath> block with \textbf{(A)}
        answer_match = re.search(
            r'(<imath>.*?\\textbf\{\(A\)\s*\}.*?</imath>)',
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
```

**Step 2: Test parser against known page**

Run: `python -c "import sys; sys.path.insert(0, 'amc-database'); from scrape import parse_problem_list; ..."`
(We'll test this live against a fetched page in Task 4.)

---

### Task 3: Parse individual solution page

**Files:**
- Modify: `amc-database/scrape.py`

**Step 1: Add solution page parser**

```python
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
    # Patterns: \boxed{\textbf{(E) } 64} or \boxed{(E)} or \boxed{\text{(E)}64}
    answer_match = re.search(
        r'\\boxed\{[^}]*\\textbf\{\(([A-E])\)',
        markup
    )
    if answer_match:
        result["answer"] = answer_match.group(1)
    else:
        # Try simpler pattern
        answer_match = re.search(r'\\boxed\{.*?\(([A-E])\)', markup)
        if answer_match:
            result["answer"] = answer_match.group(1)

    # Extract solutions — split by ==Solution headers
    sol_parts = re.split(r'==\s*Solution\s*\d*\s*(?:\([^)]*\))?\s*==', markup)
    # First part is problem, rest are solutions
    for part in sol_parts[1:]:
        # Stop at next major section (See Also, Video, etc.)
        cleaned = re.split(r'==\s*(?:See Also|Video|See also)\s*==', part, maxsplit=1)[0]
        # Remove video solution sections
        cleaned = re.split(r'==\s*Video\s+Solution', cleaned, maxsplit=1)[0]
        cleaned = cleaned.strip()
        if cleaned and len(cleaned) > 20:  # Skip near-empty solutions
            # Remove user signatures
            cleaned = re.sub(r'~+\s*\[?[^\]\n]*\]?\s*$', '', cleaned, flags=re.MULTILINE).strip()
            result["solutions"].append(cleaned)

    return result
```

---

### Task 4: Main scraping loop

**Files:**
- Modify: `amc-database/scrape.py`

**Step 1: Add main scraping function**

```python
def scrape_test(test_info: dict) -> list[dict]:
    """Scrape all problems + solutions for one test."""
    slug = test_info["slug"]
    test_name = test_info["test"]
    year = test_info["year"]
    num_problems = test_info["num_problems"]

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
                "id": f"{slug.replace('_', '_')}_P{num}",
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


def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    all_problems = []
    failed_tests = []

    # Allow filtering: python scrape.py 2023_AMC_10A
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
```

**Step 2: Test on a single test first**

Run: `cd amc-database && python scrape.py 2023_AMC_10A`

Expected: 25 problems scraped with answers and solutions, saved to `raw/2023_AMC_10A.txt` and `amc_raw.json`.

**Step 3: Verify output quality**

Spot-check: Problem 1 should be about cities A and B 45 miles apart. Answer should be "E" (27). Solutions should have readable LaTeX markup.

---

### Task 5: Run full scrape

**Step 1: Run the full scraper**

Run: `cd amc-database && python scrape.py`

Expected: ~54 tests, ~1250 problems. Will take ~30-40 min with 1.5s delays between requests (~1300 requests × 1.5s).

**Step 2: Verify completeness**

Run: `python -c "import json; d=json.load(open('amc-database/amc_raw.json')); print(f'{len(d)} problems'); ..."`

Check: count per test type, any missing answers, any empty solutions.

**Step 3: Commit**

```bash
git add amc-database/scrape.py amc-database/raw/ amc-database/amc_raw.json
git commit -m "feat: add AMC problem scraper with full 2015-2025 data"
```

---

## Notes for classifier session

Once scraping is complete, start a new Claude Code session with:
1. `amc-database/amc_raw.json` — the scraped data
2. `taxonomies/solution-architecture-taxonomy.md` — the 8 architecture types
3. `taxonomies/crossing-atlas-system.md` — cross-domain technique recognition
4. `amc-database-spec.md` — the full classification schema

That session will read each problem, classify it per the schema, and output `amc_classified.json`.
