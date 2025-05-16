from pathlib import Path
from PIL import ImageGrab

from utils import generate_random_filename, get_temp_directory


def self_screenshot(screenshot_path: Path = None) -> Path:
    if screenshot_path is None:
        screenshot_path = get_temp_directory() / generate_random_filename('png')

    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
    screenshot.close()

    return screenshot_path
