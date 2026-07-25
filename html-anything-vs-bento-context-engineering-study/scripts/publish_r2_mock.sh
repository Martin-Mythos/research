#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then echo '用法：publish_r2_mock.sh <产物目录> <暂存目录>' >&2; exit 2; fi
src=$(realpath "$1"); dst="$2"; project=$(dirname "$src")
python3 "$project/scripts/validate_artifacts.py" "$project" >/dev/null
rm -rf "$dst"; mkdir -p "$dst"
count=0
while IFS= read -r -d '' file; do rel=${file#"$src"/}; mkdir -p "$dst/$(dirname "$rel")"; cp "$file" "$dst/$rel"; sha256sum "$dst/$rel" >> "$dst/manifest.sha256"; ((count+=1)); done < <(find "$src" -type f -name '*.html' -print0 | sort -z)
printf 'Mock R2 暂存完成：%d 个 HTML 对象；目录：%s\n' "$count" "$dst"
