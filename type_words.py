import argparse
import ctypes
import re
import sys
import time
import tkinter as tk
from ctypes import wintypes
from pathlib import Path

from PIL import Image, ImageEnhance, ImageGrab, ImageOps

try:
    import pytesseract
except ImportError:
    pytesseract = None


DEFAULT_TEXT = "move make see use interest want no set too however"
INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
REGION_FILE = Path("monkeytype_region.txt")
COMMON_TESSERACT_PATHS = [
    Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
    Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
]

user32 = ctypes.WinDLL("user32", use_last_error=True)
ULONG_PTR = ctypes.c_ulonglong if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_ulong
LONG = ctypes.c_long
DWORD = ctypes.c_ulong
WORD = ctypes.c_ushort
UINT = ctypes.c_uint


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", LONG),
        ("dy", LONG),
        ("mouseData", DWORD),
        ("dwFlags", DWORD),
        ("time", DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", WORD),
        ("wScan", WORD),
        ("dwFlags", DWORD),
        ("time", DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", DWORD),
        ("wParamL", WORD),
        ("wParamH", WORD),
    ]


class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
        ("hi", HARDWAREINPUT),
    ]


class INPUT(ctypes.Structure):
    _anonymous_ = ("union",)
    _fields_ = [
        ("type", DWORD),
        ("union", INPUT_UNION),
    ]


LPINPUT = ctypes.POINTER(INPUT)
user32.SendInput.argtypes = (UINT, LPINPUT, ctypes.c_int)
user32.SendInput.restype = UINT


def _send_inputs(inputs) -> None:
    sent = user32.SendInput(len(inputs), inputs, ctypes.sizeof(INPUT))
    if sent != len(inputs):
        error_code = ctypes.get_last_error()
        raise OSError(error_code, f"SendInput failed after sending {sent} of {len(inputs)} events")


def send_unicode_character(character: str) -> None:
    code_units = character.encode("utf-16-le")

    for index in range(0, len(code_units), 2):
        code_unit = int.from_bytes(code_units[index:index + 2], "little")
        inputs = (INPUT * 2)(
            INPUT(
                type=INPUT_KEYBOARD,
                ki=KEYBDINPUT(
                    wVk=0,
                    wScan=code_unit,
                    dwFlags=KEYEVENTF_UNICODE,
                    time=0,
                    dwExtraInfo=0,
                ),
            ),
            INPUT(
                type=INPUT_KEYBOARD,
                ki=KEYBDINPUT(
                    wVk=0,
                    wScan=code_unit,
                    dwFlags=KEYEVENTF_UNICODE | KEYEVENTF_KEYUP,
                    time=0,
                    dwExtraInfo=0,
                ),
            ),
        )
        _send_inputs(inputs)


def type_text(text: str, wpm: float) -> None:
    if wpm <= 0:
        raise ValueError("WPM must be greater than 0.")

    seconds_per_character = 60 / (wpm * 5)

    for character in text:
        send_unicode_character(character)
        time.sleep(seconds_per_character)


def clean_text(text: str) -> str:
    normalized = text.lower().replace("\n", " ")
    normalized = re.sub(r"[^a-z0-9' ]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def preprocess_for_ocr(image: Image.Image) -> Image.Image:
    grayscale = ImageOps.grayscale(image)
    boosted = ImageEnhance.Contrast(grayscale).enhance(2.5)
    inverted = ImageOps.invert(boosted)
    return inverted.point(lambda value: 255 if value > 140 else 0)


def read_region_file(path: Path) -> tuple[int, int, int, int] | None:
    if not path.exists():
        return None

    parts = path.read_text(encoding="utf-8").strip().split(",")
    if len(parts) != 4:
        return None

    return tuple(int(part) for part in parts)


def write_region_file(path: Path, region: tuple[int, int, int, int]) -> None:
    path.write_text(",".join(str(value) for value in region), encoding="utf-8")


def select_screen_region() -> tuple[int, int, int, int]:
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.25)
    root.configure(background="black")
    root.title("Select Monkeytype text region")

    canvas = tk.Canvas(root, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    selection = {"start_x": 0, "start_y": 0, "rect_id": None, "region": None}

    def on_button_press(event) -> None:
        selection["start_x"] = event.x
        selection["start_y"] = event.y
        if selection["rect_id"] is not None:
            canvas.delete(selection["rect_id"])
        selection["rect_id"] = canvas.create_rectangle(
            event.x,
            event.y,
            event.x,
            event.y,
            outline="red",
            width=2,
        )

    def on_drag(event) -> None:
        if selection["rect_id"] is not None:
            canvas.coords(
                selection["rect_id"],
                selection["start_x"],
                selection["start_y"],
                event.x,
                event.y,
            )

    def on_button_release(event) -> None:
        left = min(selection["start_x"], event.x)
        top = min(selection["start_y"], event.y)
        right = max(selection["start_x"], event.x)
        bottom = max(selection["start_y"], event.y)
        selection["region"] = (left, top, right, bottom)
        root.quit()

    def on_escape(_) -> None:
        selection["region"] = None
        root.quit()

    canvas.bind("<ButtonPress-1>", on_button_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_button_release)
    root.bind("<Escape>", on_escape)

    root.mainloop()
    root.destroy()

    if not selection["region"]:
        raise RuntimeError("Region selection was cancelled.")

    left, top, right, bottom = selection["region"]
    if right - left < 20 or bottom - top < 20:
        raise RuntimeError("Selected region is too small.")

    return selection["region"]


def capture_region(region: tuple[int, int, int, int]) -> Image.Image:
    return ImageGrab.grab(bbox=region)


def ocr_image(image: Image.Image) -> str:
    if pytesseract is None:
        raise RuntimeError(
            "OCR mode requires pytesseract. Install it with `pip install pytesseract` "
            "and install Tesseract OCR for Windows."
        )

    for candidate in COMMON_TESSERACT_PATHS:
        if candidate.exists():
            pytesseract.pytesseract.tesseract_cmd = str(candidate)
            break

    processed = preprocess_for_ocr(image)
    config = "--psm 6"
    text = pytesseract.image_to_string(processed, config=config)
    cleaned = clean_text(text)
    if not cleaned:
        raise RuntimeError("OCR did not detect readable prompt text in the selected region.")
    return cleaned


def resolve_text(args) -> str:
    if args.text:
        return clean_text(args.text)

    region = None
    if args.region:
        region = tuple(args.region)
    elif args.use_saved_region:
        region = read_region_file(REGION_FILE)

    if region is None:
        print("Drag a box around the Monkeytype prompt words. Press Esc to cancel.")
        time.sleep(1)
        region = select_screen_region()
        if args.save_region:
            write_region_file(REGION_FILE, region)
            print(f"Saved region to {REGION_FILE.resolve()}")

    image = capture_region(region)
    if args.debug_image:
        image.save(args.debug_image)
        print(f"Saved screenshot to {Path(args.debug_image).resolve()}")

    detected_text = ocr_image(image)
    print(f"Detected text: {detected_text}")
    return detected_text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Type text into the focused window at a configurable WPM."
    )
    parser.add_argument(
        "--text",
        help="Text to type directly. If omitted, the script OCRs a selected screen region.",
    )
    parser.add_argument(
        "--wpm",
        type=float,
        default=60.0,
        help="Typing speed in words per minute. Standard WPM assumes 5 characters per word.",
    )
    parser.add_argument(
        "--countdown",
        type=int,
        default=5,
        help="Seconds to wait before typing starts.",
    )
    parser.add_argument(
        "--region",
        nargs=4,
        type=int,
        metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
        help="Reuse a fixed OCR region instead of drawing one.",
    )
    parser.add_argument(
        "--use-saved-region",
        action="store_true",
        help=f"Use the region saved in {REGION_FILE.name}.",
    )
    parser.add_argument(
        "--save-region",
        action="store_true",
        help=f"Save the next interactively selected region to {REGION_FILE.name}.",
    )
    parser.add_argument(
        "--debug-image",
        help="Optional path to save the captured region for OCR debugging.",
    )
    args = parser.parse_args()

    text = resolve_text(args)
    print(f"Typing in {args.countdown} seconds. Focus the target window now.")
    time.sleep(args.countdown)
    type_text(text, args.wpm)
    print("Done.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
