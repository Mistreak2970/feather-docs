#!/usr/bin/env python3
import re
from pathlib import Path

root = Path('/workspaces/feather-docs')
pattern = re.compile(r"(\.gitbook/assets/)([^)\"'<>\s]+)")

for md in root.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    new_text = text
    for m in pattern.finditer(text):
        prefix = m.group(1)
        fname = m.group(2)
        name = Path(fname).name
        stem = Path(name).stem
        ext = Path(name).suffix
        safe = re.sub(r'[^A-Za-z0-9._-]+','-', stem).strip('-') + ext
        if safe != name:
            new_text = new_text.replace(prefix+name, prefix+safe)
    if new_text != text:
        md.write_text(new_text, encoding='utf-8')
        print('Updated', md)
print('Done')
