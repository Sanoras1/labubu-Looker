import sys
import re
from pathlib import Path

# Usage: python link_finder.py input_file

def find_links(text):
    """Return a set of http/https links found in the given text."""
    return set(re.findall(r'https?://[^\s]+' , text))

def main():
    if len(sys.argv) < 2:
        print("Usage: python link_finder.py <input_file>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        print(f"Input file {input_path} not found")
        sys.exit(1)

    text = input_path.read_text()
    links = find_links(text)

    storage_path = Path("found_links.txt")
    if storage_path.exists():
        saved_links = set(storage_path.read_text().splitlines())
    else:
        saved_links = set()

    new_links = []

    for link in links:
        if link in saved_links:
            print(f"Existing link found: {link}")
        else:
            print(f"New link found: {link}")
            saved_links.add(link)
            new_links.append(link)

    if new_links:
        with storage_path.open('w') as f:
            for link in sorted(saved_links):
                f.write(link + '\n')
        print(f"Saved {len(new_links)} new link(s) to {storage_path}")
    else:
        print("No new links found.")

if __name__ == '__main__':
    main()
