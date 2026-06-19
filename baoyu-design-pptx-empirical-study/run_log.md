# Run Log

Date: 2026-06-19

## Local Deck

Input deck:

- `artifacts/local_deck/index.html`
- `artifacts/local_deck/config-editable.json`
- `artifacts/local_deck/imagegen-server-room.png`

The deck contains:

- Slide 1: design-system style prompt and gradient/card layout.
- Slide 2: design token grid with native text and shape-heavy layout.
- Slide 3: local image generation PNG insertion, plus editable labels and bullet text.

## Static Server

```bash
cd baoyu-design-pptx-empirical-study/artifacts/local_deck
python3 -m http.server 8787 --bind 127.0.0.1
```

## Baoyu Editable PPTX Export

```bash
cd /tmp/baoyu-design-local/skills/baoyu-design/agents/gen-pptx
node dist/cli.mjs \
  --url http://127.0.0.1:8787/index.html \
  --config /Users/martin/Library/CloudStorage/GoogleDrive-martin.lanse2000@gmail.com/我的云端硬盘/workspace_sync/assets/Work-PKM-Vault/baoyu-design-pptx-empirical-study/artifacts/local_deck/config-editable.json \
  --out /Users/martin/Library/CloudStorage/GoogleDrive-martin.lanse2000@gmail.com/我的云端硬盘/workspace_sync/assets/Work-PKM-Vault/baoyu-design-pptx-empirical-study/artifacts
```

CLI result:

```json
{
  "ok": true,
  "file": "baoyu-design-pptx-empirical-study/artifacts/baoyu-design-imagegen-editable.pptx",
  "slides": 3,
  "bytes": 2478623,
  "flags": [],
  "warnings": [],
  "speakerNotes": [
    "Slide 1 speaker notes: design-system prompt baseline.",
    "Slide 2 speaker notes: token capture and editability inspection.",
    "Slide 3 speaker notes: local image generation insertion workflow."
  ]
}
```

## Evidence Commands

OOXML inspection:

```bash
python3 - <<'PY'
from zipfile import ZipFile
from pathlib import Path
import re, json

pptx = Path("baoyu-design-pptx-empirical-study/artifacts/baoyu-design-imagegen-editable.pptx")
with ZipFile(pptx) as z:
    slide_names = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)])
    for n in slide_names:
        xml = z.read(n).decode("utf-8", errors="replace")
        print(n, xml.count("<p:txBody>"), xml.count("<p:sp>"), xml.count("<p:pic>"), xml.count("<a:t>"))
PY
```

Result:

```text
ppt/slides/slide1.xml p:txBody=5  p:sp=6   p:pic=1  a:t=6
ppt/slides/slide2.xml p:txBody=16 p:sp=27  p:pic=0  a:t=16
ppt/slides/slide3.xml p:txBody=5  p:sp=7   p:pic=1  a:t=7
```

LibreOffice PDF export:

```bash
soffice --headless --convert-to pdf \
  --outdir baoyu-design-pptx-empirical-study/screenshots \
  baoyu-design-pptx-empirical-study/artifacts/baoyu-design-imagegen-editable.pptx
```

Result:

- `screenshots/baoyu-design-imagegen-editable.pdf`
