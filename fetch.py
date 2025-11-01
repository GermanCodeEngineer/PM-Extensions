import requests
import os

def fetch_js(url, filename=None):
    # Get JS content
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request failed
    js_code = response.text

    # Determine filename
    if filename is None:
        # Extract from URL or default
        filename = os.path.basename(url) or "downloaded.js"
        if not filename.endswith(".js"):
            filename += ".js"

    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    # Save file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"✅ Saved JavaScript to {filepath}")

if __name__ == "__main__":
    url = input("Enter the JS file URL: ").strip()
    fetch_js(url)