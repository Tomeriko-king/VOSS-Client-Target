import string

from PIL import ImageGrab
import random


def generate_screenshot_name() -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)) + '.png'


def self_screenshot(screenshot_filename: str = None) -> str:
    if screenshot_filename is None:
        screenshot_filename = generate_screenshot_name()

    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_filename)
    screenshot.close()

    return screenshot_filename
