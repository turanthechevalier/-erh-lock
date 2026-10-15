#!/usr/bin/env bash
# Kitabı Markdown kaynaklarından DOCX ve PDF olarak derler.
# Gereksinimler: pandoc (>= 3), LibreOffice, python3 + python-docx, pypdf
set -euo pipefail

KOK="$(cd "$(dirname "$0")" && pwd)"
CIKTI="$KOK/cikti"
mkdir -p "$CIKTI"

python3 "$KOK/araclar/referans_olustur.py" \
  "$KOK/araclar/varsayilan-referans.docx" "$CIKTI/referans.docx"

pandoc \
  --from markdown+smart \
  --metadata-file "$KOK/metadata.yaml" \
  --reference-doc "$CIKTI/referans.docx" \
  --toc --toc-depth 2 \
  -o "$CIKTI/bekcileri-kim-bekleyecek.docx" \
  "$KOK"/bolumler/*.md

if [[ "${1:-}" != "--yalniz-docx" ]]; then
  python3 "$KOK/araclar/pdf_cevir.py" \
    "$CIKTI/bekcileri-kim-bekleyecek.docx" "$CIKTI/bekcileri-kim-bekleyecek.pdf"
  python3 - "$CIKTI/bekcileri-kim-bekleyecek.pdf" <<'PY'
import sys
from pypdf import PdfReader
print("Sayfa sayısı:", len(PdfReader(sys.argv[1]).pages))
PY
fi
cat "$KOK"/bolumler/*.md | wc -w | xargs echo "Kelime sayısı (kaynak):"
