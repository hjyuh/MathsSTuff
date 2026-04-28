# AMC Database — Scraper Design
## Date: 2026-03-23

## Scope

One Python script (`amc-database/scrape.py`) that scrapes all AMC 8/10A/10B/12A/12B problems and solutions from AoPS wiki (2015–2025) and outputs structured raw data for a separate classification session.

## Data Source

AoPS Wiki. URL patterns:
- Problem list: `https://artofproblemsolving.com/wiki/index.php/{YEAR}_AMC_{TYPE}_Problems`
- Individual problem+solution: `https://artofproblemsolving.com/wiki/index.php/{YEAR}_AMC_{TYPE}_Problems/Problem_{N}`

## Tests to Scrape

- AMC 8: 2015–2019, 2021–2025 (2020 cancelled due to COVID)
- AMC 10A/10B: 2015–2025
- AMC 12A/12B: 2015–2025
- Total: ~50 tests, ~1250 problems

## Output

1. **Raw text files** in `amc-database/raw/` — one per test (e.g., `2023_AMC10A.txt`)
2. **`amc-database/amc_raw.json`** — flat array of all problems:
   ```json
   {
     "id": "2023_AMC10A_P18",
     "test": "AMC 10A",
     "year": 2023,
     "number": 18,
     "problem": "...",
     "choices": {"A": "...", "B": "...", "C": "...", "D": "...", "E": "..."},
     "answer": "C",
     "solutions": ["Solution 1...", "Solution 2..."]
   }
   ```

## Scraping Strategy

- Use `requests` + `BeautifulSoup` (standard Python libraries)
- Polite rate limiting: 1-2 second delay between requests
- Retry logic for transient failures
- Progress logging to stdout
- Save raw HTML as well for debugging if needed

## Classification (separate session)

A second Claude Code session will read `amc_raw.json` + Mahmoud's taxonomy files (solution architecture, crossing atlas, technique lists) and produce the classified database with all fields from `amc-database-spec.md`.

## Decision Log

- No API-based classification — Mahmoud will run a dedicated Claude Code session with taxonomy context
- Scrape AoPS wiki HTML (not PDFs) — has both problems and solutions in clean text
- Three-stage pipeline simplified to one scrape script + separate classification session
