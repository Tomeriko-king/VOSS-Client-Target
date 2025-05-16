import random
import string
import tempfile
from pathlib import Path


def generate_random_filename(extension='', n=16) -> str:
    if extension:
        extension = '.' + extension

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n)) + extension


def get_temp_directory() -> Path:
    return Path(tempfile.gettempdir())


print(get_temp_directory())
