# labubu-Looker

Utilities for capturing screenshots of web pages and locating images on the
screen. The project relies on `pyautogui` for locating images and capturing
screenshots while using Pillow (PIL) for saving them.

## Features

- Open a web page in the default browser.
- Capture a screenshot and save it to disk.
- Search the current screen for a given image.

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Example

```python
from looker import open_webpage, capture_screen, find_image

open_webpage("https://example.com")

# Save a screenshot
capture_screen("page.png")

# Search for an image on the screen
location = find_image("button.png")
if location:
    print(f"Found at {location}")
```
