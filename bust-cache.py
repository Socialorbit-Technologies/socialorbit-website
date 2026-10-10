#!/usr/bin/env python3
"""Content-hash cache-busting. Run after editing css/js:  python3 bust-cache.py
Rewrites every  css/site.css?v=...  and  js/site.js?v=...  in all *.html files
with the first 10 chars of the file's SHA-256, so a deploy never serves stale assets."""
import hashlib, pathlib, re
root = pathlib.Path(__file__).resolve().parent
assets = ["css/site.css", "js/site.js"]
hashes = {a: hashlib.sha256((root / a).read_bytes()).hexdigest()[:10] for a in assets}
for page in root.rglob("*.html"):
    s = page.read_text(encoding="utf-8")
    for a, h in hashes.items():
        s = re.sub(re.escape(a) + r"\?v=[^\"']*", f"{a}?v={h}", s)
    page.write_text(s, encoding="utf-8")
    print(f"updated {page.relative_to(root)}")
print(hashes)
