# CIA Pipeline Automator v5
# Automates copy-paste relay between GPT 5.2 Pro and GPT 5.4 Pro
# GUI automation on subscription — no API needed
#
# SETUP:
# 1. pip install pyautogui pyperclip pynput
# 2. Open Chrome with TWO tabs: 5.2 Pro (tab 1), 5.4 Pro (tab 2)
# 3. Maximize Chrome
# 4. python pipeline.py calibrate
# 5. python pipeline.py stats
# 6. python pipeline.py run

import pyautogui
import pyperclip
import time
import sys
import json
import os
from datetime import datetime

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True  # top-left corner = abort

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pipeline_coords.json")
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pipeline_logs")

WAIT_54_PRO = 3600       # 5.4 Pro: up to 60 min
WAIT_52_PRO = 600        # 5.2 Pro: up to 10 min
POLL_INTERVAL = 30       # check every 30 seconds (less aggressive)
SCROLL_HOLD_TIME = 3
MAX_ROUNDS = 20
COPY_RETRIES = 5

# Sentinel value — we set clipboard to this before waiting
# so we can tell "no new copy" from "copied empty"
CLIPBOARD_SENTINEL = "___CIA_PIPELINE_WAITING___"


# ============================================================
# CONFIG
# ============================================================

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


# ============================================================
# CALIBRATION
# ============================================================

def wait_for_click():
    from pynput import mouse
    click_pos = {"x": None, "y": None, "done": False}
    
    def on_click(x, y, button, pressed):
        if pressed and not click_pos["done"]:
            click_pos["x"] = x
            click_pos["y"] = y
            click_pos["done"] = True
            return False
    
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    while not click_pos["done"]:
        time.sleep(0.05)
    listener.stop()
    return click_pos["x"], click_pos["y"]


def calibrate():
    elements = [
        ("tab_52", "the GPT 5.2 Pro BROWSER TAB"),
        ("tab_54", "the GPT 5.4 Pro BROWSER TAB"),
        ("input_box", "the ChatGPT INPUT BOX (where you type messages)"),
        ("send_button", "the SEND BUTTON (arrow icon)"),
        ("copy_area", "the GAP between the input box and the response buttons (NOT on any button)"),
    ]
    
    print("\n=== CIA PIPELINE CALIBRATION v5 ===")
    print("For each element:")
    print("  1. Press ENTER here in the terminal")
    print("  2. Switch to browser and click on the element")
    print("  3. Position is recorded automatically\n")
    print("NOTE: For 'copy_area', click in the EMPTY SPACE between")
    print("the input box and the row of buttons (copy/thumbs/etc).\n")
    
    config = load_config()
    
    for key, description in elements:
        existing = config.get(key)
        if existing:
            print(f"  [{key}] Current: ({existing['x']}, {existing['y']})")
        
        print(f">>> Press ENTER, then click on {description}")
        input("    Ready? Press ENTER... ")
        
        print("    Listening for click...")
        x, y = wait_for_click()
        config[key] = {"x": x, "y": y}
        print(f"    Recorded: ({x}, {y})\n")
    
    save_config(config)
    print(f"Saved to {CONFIG_FILE}\n")
    print("=== CALIBRATION COMPLETE ===")
    for key, pos in config.items():
        print(f"  {key}: ({pos['x']}, {pos['y']})")
    print(f"\nNext: python pipeline.py stats")


def recalibrate_one():
    config = load_config()
    if not config:
        print("No config. Run 'python pipeline.py calibrate' first.")
        return
    
    keys = list(config.keys())
    print("\nWhich element?")
    for i, key in enumerate(keys):
        pos = config[key]
        print(f"  {i+1}. {key} ({pos['x']}, {pos['y']})")
    
    choice = input("\nNumber or name: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(keys):
        key = keys[int(choice) - 1]
    elif choice in config:
        key = choice
    else:
        print(f"Unknown: {choice}")
        return
    
    print(f"\n>>> Press ENTER, then click new position for [{key}]")
    input("    Ready? Press ENTER... ")
    print("    Listening...")
    x, y = wait_for_click()
    config[key] = {"x": x, "y": y}
    save_config(config)
    print(f"    Updated {key}: ({x}, {y})")


# ============================================================
# STATS
# ============================================================

def stats():
    config = load_config()
    if not config:
        print("No config. Run 'python pipeline.py calibrate' first.")
        return
    
    print("\n=== COORDINATE VERIFICATION ===")
    print("Mouse moves to each position (NO clicking).\n")
    
    for key, pos in config.items():
        print(f"  [{key}] at ({pos['x']}, {pos['y']})")
        input("    Press ENTER to move mouse there... ")
        pyautogui.moveTo(pos['x'], pos['y'], duration=0.5)
        
        ok = input("    Correct? [y/n/skip]: ").strip().lower()
        if ok == 'n':
            print(f"    >>> Press ENTER then click correct position for [{key}]")
            input("    Ready? Press ENTER... ")
            print("    Listening...")
            x, y = wait_for_click()
            config[key] = {"x": x, "y": y}
            save_config(config)
            print(f"    Updated: ({x}, {y})\n")
        else:
            print()
    
    print("=== FINAL COORDINATES ===")
    for key, pos in config.items():
        print(f"  {key}: ({pos['x']}, {pos['y']})")


# ============================================================
# CORE ACTIONS
# ============================================================

def switch_to_tab(config, tab_name):
    pos = config[tab_name]
    pyautogui.click(pos['x'], pos['y'])
    time.sleep(1.5)


def scroll_to_bottom():
    pyautogui.press('end')
    time.sleep(0.5)
    pyautogui.keyDown('pagedown')
    time.sleep(SCROLL_HOLD_TIME)
    pyautogui.keyUp('pagedown')
    time.sleep(1)


def click_input_box(config):
    pos = config['input_box']
    pyautogui.click(pos['x'], pos['y'])
    time.sleep(0.5)


def type_and_send(config, text):
    click_input_box(config)
    time.sleep(0.3)
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pos = config['send_button']
    pyautogui.click(pos['x'], pos['y'])
    time.sleep(1)


def try_copy(config):
    """
    Attempt to copy the last response once.
    Scrolls to bottom, clicks the gap, Tab, Enter.
    Returns clipboard content (may be sentinel if copy failed).
    """
    scroll_to_bottom()
    time.sleep(1)
    
    pos = config['copy_area']
    pyautogui.click(pos['x'], pos['y'])
    time.sleep(0.5)
    
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.press('enter')
    time.sleep(1)
    
    return pyperclip.paste()


def copy_last_response(config, previous_content=""):
    """
    Copy the last ChatGPT response. Retries until clipboard has 
    genuinely NEW content (different from previous_content and sentinel).
    """
    pyperclip.copy(CLIPBOARD_SENTINEL)
    
    for attempt in range(COPY_RETRIES):
        result = try_copy(config)
        
        # Check: is this genuinely new content?
        if (result 
            and result != CLIPBOARD_SENTINEL 
            and result != previous_content 
            and len(result) > 20):
            print(f"    Copy success (attempt {attempt+1}, {len(result)} chars)")
            return result
        
        print(f"    Copy attempt {attempt+1}: no new content, retrying...")
        time.sleep(2)
    
    # All retries failed
    result = pyperclip.paste()
    if result and result != CLIPBOARD_SENTINEL and len(result) > 20:
        return result
    
    print("    !!! Copy FAILED after all retries")
    return None


def wait_for_response(config, timeout, previous_clipboard=""):
    """
    Wait for model to finish responding.
    
    KEY FIX (v5): We set clipboard to a sentinel BEFORE polling.
    We only declare "done" when:
      1. Clipboard has NEW content (not sentinel, not previous_clipboard)
      2. That new content is stable across 2 consecutive polls
    
    This prevents the old bug where stale clipboard content from a 
    previous step was mistaken for a completed response.
    """
    print(f"    Waiting (max {timeout//60}min, polling every {POLL_INTERVAL}s)...")
    start = time.time()
    
    # Set sentinel so we can detect genuine new copies
    pyperclip.copy(CLIPBOARD_SENTINEL)
    
    last_new_content = ""
    stable_count = 0
    
    # Initial wait — don't spam while model is clearly still starting
    initial_wait = min(60, timeout)
    print(f"    Initial wait: {initial_wait}s before first poll...")
    time.sleep(initial_wait)
    
    while time.time() - start < timeout:
        elapsed = int(time.time() - start)
        mins = elapsed // 60
        secs = elapsed % 60
        print(f"    ... {mins}m {secs:02d}s elapsed (stable: {stable_count}/2)   ", end='\r')
        
        # Try to copy
        # Reset sentinel before each attempt so we know if copy worked
        pyperclip.copy(CLIPBOARD_SENTINEL)
        time.sleep(0.5)
        
        result = try_copy(config)
        
        # Is this genuinely new content?
        is_new = (
            result 
            and result != CLIPBOARD_SENTINEL
            and result != previous_clipboard
            and len(result) > 20
        )
        
        if is_new:
            if result == last_new_content:
                stable_count += 1
                if stable_count >= 2:
                    elapsed_final = int(time.time() - start)
                    print(f"\n    Response complete! ({elapsed_final}s, {len(result)} chars)")
                    return result
            else:
                # New content but different from last poll — model still generating
                stable_count = 0
                last_new_content = result
                print(f"\n    ... response growing ({len(result)} chars so far)")
        else:
            # Copy failed or got sentinel — model probably still generating
            stable_count = 0
        
        time.sleep(POLL_INTERVAL)
    
    # Timeout — try one final copy
    print(f"\n    Timeout ({timeout}s). Final copy attempt...")
    pyperclip.copy(CLIPBOARD_SENTINEL)
    time.sleep(1)
    result = try_copy(config)
    
    if result and result != CLIPBOARD_SENTINEL and result != previous_clipboard and len(result) > 20:
        print(f"    Got response on final attempt ({len(result)} chars)")
        return result
    
    print("    !!! No response captured after timeout")
    return None


# ============================================================
# LOGGING
# ============================================================

def log_round(round_num, prompt, response, model):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(LOG_DIR, f"round_{round_num:03d}_{model}_{timestamp}.md")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Round {round_num} — {model}\n")
        f.write(f"## Timestamp: {timestamp}\n\n")
        f.write(f"## Prompt\n```\n{str(prompt)[:500]}...\n```\n\n")
        f.write(f"## Response\n{response}\n")
    return filename


# ============================================================
# PROMPT EXTRACTION
# ============================================================

def extract_next_prompt(conductor_response):
    markers = ['NEXT PROMPT:', '**NEXT PROMPT:**', '**NEXT PROMPT**:', 'NEXT PROMPT']
    for marker in markers:
        if marker in conductor_response:
            idx = conductor_response.index(marker) + len(marker)
            prompt = conductor_response[idx:].strip()
            if prompt.startswith('```'):
                end = prompt.find('```', 3)
                if end > 0:
                    prompt = prompt[3:end].strip()
            for stop in ['STATUS UPDATE:', '**STATUS UPDATE', 'GAPS:', '**GAPS**']:
                if stop in prompt:
                    prompt = prompt[:prompt.index(stop)].strip()
            return prompt
    return None


# ============================================================
# MAIN PIPELINE
# ============================================================

def run_pipeline(config):
    print("\n=== CIA PIPELINE v5 ===")
    print(f"Rounds: {MAX_ROUNDS}")
    print(f"5.4 timeout: {WAIT_54_PRO//60}min | 5.2 timeout: {WAIT_52_PRO//60}min")
    print(f"Poll interval: {POLL_INTERVAL}s | Copy retries: {COPY_RETRIES}")
    print(f"Logs: {LOG_DIR}")
    print()
    print("FIX IN v5: Sentinel-based clipboard tracking.")
    print("Old clipboard content can no longer be mistaken for a new response.")
    print()
    print("Mouse to TOP-LEFT CORNER to abort.")
    print("Starting in 5 seconds...\n")
    time.sleep(5)
    
    # Track what's on clipboard to prevent confusion between rounds
    last_known_clipboard = ""
    
    for rnd in range(1, MAX_ROUNDS + 1):
        print(f"\n{'='*60}")
        print(f"ROUND {rnd}")
        print(f"{'='*60}")
        
        # --- 5.2 Pro: get next prompt ---
        print("\n[1] → 5.2 Pro tab")
        switch_to_tab(config, "tab_52")
        
        if rnd > 1:
            print("[2] Waiting for 5.2 to evaluate...")
            conductor_resp = wait_for_response(config, WAIT_52_PRO, last_known_clipboard)
            if conductor_resp is None:
                print("!!! 5.2 response capture failed. Manual intervention needed.")
                break
        else:
            print("[2] First round — copying 5.2's existing response...")
            conductor_resp = copy_last_response(config, last_known_clipboard)
            if conductor_resp is None:
                print("!!! Could not copy 5.2's response. Check calibration.")
                break
        
        log_round(rnd, "conductor", conductor_resp, "52pro")
        last_known_clipboard = conductor_resp
        
        next_prompt = extract_next_prompt(conductor_resp)
        if next_prompt is None:
            print("\n!!! No 'NEXT PROMPT:' found in 5.2's response.")
            print(f"!!! Preview: {conductor_resp[:300]}")
            print("!!! Manual intervention needed.")
            break
        
        print(f"[3] Extracted prompt ({len(next_prompt)} chars)")
        print(f"    Preview: {next_prompt[:80]}...")
        
        # --- 5.4 Pro: send and wait ---
        print("\n[4] → 5.4 Pro tab")
        switch_to_tab(config, "tab_54")
        
        print("[5] Sending prompt to 5.4 Pro...")
        type_and_send(config, next_prompt)
        
        print("[6] Waiting for 5.4 Pro Extended Thinking...")
        solver_resp = wait_for_response(config, WAIT_54_PRO, last_known_clipboard)
        if solver_resp is None:
            print("!!! 5.4 response capture failed. Manual intervention needed.")
            break
        
        log_round(rnd, next_prompt, solver_resp, "54pro")
        last_known_clipboard = solver_resp
        print(f"[7] Got 5.4 response ({len(solver_resp)} chars)")
        
        # --- Relay back to 5.2 ---
        print("\n[8] → 5.2 Pro tab")
        switch_to_tab(config, "tab_52")
        
        print("[9] Relaying 5.4 response to 5.2...")
        type_and_send(config, f"5.4 Pro responded:\n\n{solver_resp}")
        
        print(f"\n--- Round {rnd} complete ---")
    
    print(f"\n=== PIPELINE COMPLETE ===")


# ============================================================
# TEST
# ============================================================

def test_copy(config):
    print("=== TEST: Scroll + Tab Copy ===")
    print("Go to a ChatGPT tab with a response visible.")
    input("Press ENTER when ready... ")
    
    print("\nClearing clipboard with sentinel...")
    pyperclip.copy(CLIPBOARD_SENTINEL)
    
    print("Scrolling to bottom...")
    scroll_to_bottom()
    time.sleep(1)
    
    print("Clicking copy_area...")
    pos = config['copy_area']
    pyautogui.click(pos['x'], pos['y'])
    time.sleep(0.5)
    
    print("Tab...")
    pyautogui.press('tab')
    time.sleep(0.3)
    
    print("Enter...")
    pyautogui.press('enter')
    time.sleep(1)
    
    text = pyperclip.paste()
    
    if text == CLIPBOARD_SENTINEL:
        print("\n!!! FAILED: Clipboard still has sentinel. Copy didn't work.")
        print("!!! The Tab+Enter probably didn't hit the copy button.")
        print("!!! Recalibrate copy_area: python pipeline.py recal")
    elif len(text) < 20:
        print(f"\n!!! SUSPICIOUS: Only {len(text)} chars copied.")
        print(f"!!! Content: '{text}'")
    else:
        print(f"\nSUCCESS: {len(text)} chars copied")
        print(f"First 200: {text[:200]}")
        if len(text) > 200:
            print(f"Last 100: ...{text[-100:]}")


def test_full_cycle(config):
    print("=== TEST: Full Cycle ===")
    print("Make sure both tabs have existing responses.\n")
    input("Press ENTER to start... ")
    
    print("[1] → tab 1 (5.2)...")
    switch_to_tab(config, "tab_52")
    time.sleep(1)
    
    print("[2] Copying from tab 1...")
    text1 = copy_last_response(config)
    
    print(f"\n[3] → tab 2 (5.4)...")
    switch_to_tab(config, "tab_54")
    time.sleep(1)
    
    print("[4] Copying from tab 2...")
    text2 = copy_last_response(config, text1 or "")
    
    print(f"\n=== RESULTS ===")
    if text1:
        print(f"Tab 1: SUCCESS ({len(text1)} chars)")
        print(f"  Preview: {text1[:100]}...")
    else:
        print(f"Tab 1: FAILED")
    
    if text2:
        print(f"Tab 2: SUCCESS ({len(text2)} chars)")
        print(f"  Preview: {text2[:100]}...")
    else:
        print(f"Tab 2: FAILED")
    
    if text1 and text2:
        if text1 == text2:
            print("\n!!! WARNING: Both tabs returned IDENTICAL content.")
            print("!!! The copy from tab 2 might have gotten tab 1's stale clipboard.")
        else:
            print("\nBoth unique. Pipeline ready!")
    else:
        print("\nSomething failed. Recalibrate: python pipeline.py recal")


# ============================================================
# MAIN
# ============================================================

def main():
    if len(sys.argv) < 2:
        print("CIA Pipeline Automator v5")
        print()
        print("Commands:")
        print("  calibrate  — record positions (Enter → click)")
        print("  stats      — verify positions (mouse moves, no click)")
        print("  recal      — redo one position")
        print("  test       — test copy on current tab")
        print("  testcycle  — test copy across both tabs")
        print("  run        — start the automated pipeline")
        return
    
    cmd = sys.argv[1].lower()
    
    if cmd == "calibrate":
        calibrate()
    elif cmd == "stats":
        stats()
    elif cmd == "recal":
        recalibrate_one()
    elif cmd == "test":
        config = load_config()
        if not config:
            print("Calibrate first: python pipeline.py calibrate")
            return
        test_copy(config)
    elif cmd == "testcycle":
        config = load_config()
        if not config:
            print("Calibrate first: python pipeline.py calibrate")
            return
        test_full_cycle(config)
    elif cmd == "run":
        config = load_config()
        if not config:
            print("Calibrate first: python pipeline.py calibrate")
            return
        run_pipeline(config)
    else:
        print(f"Unknown: {cmd}")


if __name__ == "__main__":
    main()
