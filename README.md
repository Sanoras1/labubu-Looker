# labubu-Looker

Simple utility to scan a text file for HTTP/HTTPS links. All discovered links
are stored in `found_links.txt`. If a link already exists in that file the
script prints a message to alert the user.

## Usage

```bash
python link_finder.py path/to/file.txt
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
