"""Utilities for interacting with web pages via screenshots and image searches."""

from .webpage import open_webpage
from .screen import capture_screen
from .search import find_image

__all__ = ["open_webpage", "capture_screen", "find_image"]
