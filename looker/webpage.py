"""Module for opening web pages."""

import webbrowser


def open_webpage(url: str) -> None:
    """Open the provided URL in the default system browser."""
    webbrowser.open(url)
