#!/usr/bin/env python3
"""
Task 3: Download all images from Squarespace CDN into src/assets/images/.

- Parses every .html in backup-squarespace-original/
- Extracts unique image URLs from images.squarespace-cdn.com
- Downloads each, deriving a clean filename from the URL
  (last path segment + project prefix to avoid name collisions)
- Maps each image back to the project it came from for the manifest
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from collections import defaultdict

BACKUP = Path("/Users/balduinallroggen/Documents/PortfolioWebsite/backup-squarespace-original")
OUT    = Path("/Users/balduinallroggen/Documents/PortfolioWebsite/balduin.me.rebuilt/src/assets/images")
OUT.mkdir(parents=True, exist_ok=True)

# Project slug -> prefix used in filenames
PROJECT_PREFIX = {
    "index.html":                 "home",
    "a-planet-on-fire.html":      "apof",
    "endstation.html":            "endstation",
    "next-level-pioneers.html":   "nlp",
    "next-level-pioneers-1.html": "romanesco",
    # dead pages we ignore:
    "cart.html":                  None,
    "_downloads.html":            None,
    "_00.txt":                    None,
}

URL_RE = re.compile(r"https://images\.squarespace-cdn\.com/content/[^\"'\s?]+")

def safe_name(prefix: str, url: str) -> str:
    # Last path segment is the actual file
    path = urllib.parse.urlparse(url).path
    basename = path.rsplit("/", 1)[-1]
    # Squarespace sometimes appends a content token; basename already excludes that
    return f"{prefix}-{basename}" if prefix else basename

def download(url: str, dest: Path) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    dest.write_bytes(data)
    return True

# Collect (project, url) pairs
images_by_project = defaultdict(set)
for html_file in BACKUP.glob("*.html"):
    prefix = PROJECT_PREFIX.get(html_file.name)
    if prefix is None:
        continue
    text = html_file.read_text(errors="replace")
    for url in URL_RE.findall(text):
        images_by_project[prefix].add(url)

# Download everything
manifest = {}
errors = []
for project, urls in images_by_project.items():
    manifest[project] = []
    for url in sorted(urls):
        name = safe_name(project, url)
        dest = OUT / name
        if dest.exists() and dest.stat().st_size > 0:
            manifest[project].append({"src": f"/assets/images/{name}", "original": url, "cached": True})
            continue
        try:
            download(url, dest)
            manifest[project].append({"src": f"/assets/images/{name}", "original": url, "cached": False})
            print(f"  ✓ {project:12s} {name}")
        except Exception as e:
            errors.append((project, url, str(e)))
            print(f"  ✗ {project:12s} {url}  → {e}", file=sys.stderr)

# Save manifest for the next task (project page extraction)
(OUT / "_manifest.json").write_text(json.dumps(manifest, indent=2))

print(f"\nDownloaded {sum(len(v) for v in manifest.values())} images across {len(manifest)} projects")
if errors:
    print(f"  {len(errors)} errors (see above)")
    sys.exit(1)
