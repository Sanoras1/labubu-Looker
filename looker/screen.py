"""Utilities for capturing screenshots using pyautogui and saving them with PIL."""

import pyautogui


def capture_screen(save_path: str) -> None:
    """Capture the current screen and save the image to ``save_path``."""
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
