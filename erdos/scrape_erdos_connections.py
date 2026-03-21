"""
Erdős Problem Connection Scraper
Scrapes erdosproblems.com for "See also" links between problems.
Outputs a JSON file that can be loaded into the graph visualization.

Usage: python scrape_erdos_connections.py
Output: erdos_connections.json
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
import sys

BASE = "https://www.erdosproblems.com"
HEADERS = {"User-Agent": "ErdosGraphProject/1.0 (research)"}

def get_all_problem_ids():
    """Get all problem IDs from the main page."""
    print("Fetching problem list...")
    resp = requests.get(f"{BASE}/all", headers=HEADERS, timeout=30)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    ids = set()
    # Look for links to individual problems
    for a in soup.find_all("a", href=True):
        m = re.match(r"^/(\d+)$", a["href"])
        if m:
            ids.add(int(m.group(1)))
    
    print(f"Found {len(ids)} problems")
    return sorted(ids)

def scrape_problem(pid):
    """Scrape a single problem page for status, topic, and connections."""
    url = f"{BASE}/{pid}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return None
        soup = BeautifulSoup(resp.text, "html.parser")
        
        # Extract status from the page
        status = "open"
        status_el = soup.find(string=re.compile(r"PROVED|DISPROVED|OPEN|SOLVED", re.I))
        if status_el:
            s = status_el.strip().upper()
            if "PROVED" in s and "LEAN" in s:
                status = "proved_lean"
            elif "PROVED" in s:
                status = "proved"
            elif "DISPROVED" in s:
                status = "disproved"
            elif "SOLVED" in s:
                status = "proved"
        
        # Extract topic tags
        topic = "unknown"
        for tag_el in soup.find_all(string=re.compile(r"number theory|combinatorics|graph theory|geometry|probability", re.I)):
            t = tag_el.strip().lower()
            if "number theory" in t: topic = "number theory"
            elif "combinatorics" in t: topic = "combinatorics"
            elif "graph theory" in t: topic = "graph theory"
            elif "geometry" in t: topic = "geometry"
            elif "probability" in t: topic = "probability"
            break
        
        # Extract "See also" connections
        links = []
        text = soup.get_text()
        see_also = re.findall(r"See also.*?\[(\d+)\]", text)
        for ref in see_also:
            links.append(int(ref))
        
        # Also look for bracket references in problem text
        for a in soup.find_all("a", href=True):
            m = re.match(r"^/(\d+)$", a["href"])
            if m:
                ref_id = int(m.group(1))
                if ref_id != pid and ref_id not in links:
                    # Check if it's in a "See also" context
                    parent_text = a.parent.get_text() if a.parent else ""
                    if "See also" in parent_text or "see also" in parent_text:
                        links.append(ref_id)
        
        return {
            "id": pid,
            "status": status,
            "topic": topic,
            "links": sorted(set(links))
        }
    except Exception as e:
        print(f"  Error on #{pid}: {e}")
        return None

def main():
    # Option 1: Scrape everything (slow, ~20 min with rate limiting)
    # Option 2: Use the GitHub YAML (faster if available)
    
    print("=" * 50)
    print("Erdős Problem Connection Scraper")
    print("=" * 50)
    
    # Try to get problem IDs
    try:
        all_ids = get_all_problem_ids()
    except Exception as e:
        print(f"Failed to get problem list: {e}")
        print("Using fallback range 1-1200...")
        all_ids = list(range(1, 1201))
    
    problems = []
    total = len(all_ids)
    
    for i, pid in enumerate(all_ids):
        if i % 50 == 0:
            print(f"Progress: {i}/{total} ({100*i//total}%)")
        
        data = scrape_problem(pid)
        if data:
            problems.append(data)
        
        # Rate limit: 0.5 second between requests
        time.sleep(0.5)
    
    print(f"\nScraped {len(problems)} problems successfully")
    
    # Count connections
    total_edges = sum(len(p["links"]) for p in problems) // 2
    print(f"Found {total_edges} connections")
    
    # Save to JSON
    output = {
        "scraped_at": time.strftime("%Y-%m-%d %H:%M"),
        "total_problems": len(problems),
        "total_connections": total_edges,
        "problems": problems
    }
    
    with open("erdos_connections.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"Saved to erdos_connections.json")
    
    # Also generate JS format for direct embedding
    js_array = "const PROBLEMS = " + json.dumps(problems, indent=2) + ";"
    with open("erdos_problems_data.js", "w") as f:
        f.write(js_array)
    
    print(f"Saved JS data to erdos_problems_data.js")
    print(f"\nTo use: replace the PROBLEMS array in erdos-graph.html with the contents of erdos_problems_data.js")

if __name__ == "__main__":
    main()
