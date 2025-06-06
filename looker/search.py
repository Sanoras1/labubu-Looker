"""Image searching utilities powered by pyautogui."""

from typing import Optional

import pyautogui


def find_image(image_path: str, confidence: float = 0.9) -> Optional[pyautogui.Box]:
    """Return the region where ``image_path`` is found on screen or ``None``."""
    try:
        return pyautogui.locateOnScreen(image_path, confidence=confidence)
    except Exception:
        return None
