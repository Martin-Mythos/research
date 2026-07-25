#!/usr/bin/env bash
set -euo pipefail

DEST=${1:?usage: install_pinned_loopkit.sh DEST [CACHE_DIR]}
CACHE_DIR=${2:-/tmp/loopkit-pinned-source}
REPO=https://github.com/Archive228/loopkit.git
COMMIT=22101ff114cbf80bf3d14d41c8c662f507b1b971
mkdir -p "$DEST"

if [ ! -d "$CACHE_DIR/.git" ]; then
  git clone "$REPO" "$CACHE_DIR"
fi
git -C "$CACHE_DIR" fetch origin
git -C "$CACHE_DIR" checkout --detach "$COMMIT"

copy_missing() {
  local source=$1 destination=$2
  if [ ! -e "$destination" ]; then
    mkdir -p "$(dirname "$destination")"
    cp "$source" "$destination"
  fi
}

while IFS= read -r source; do
  relative=${source#"$CACHE_DIR/.claude/"}
  copy_missing "$source" "$DEST/.claude/$relative"
done < <(find "$CACHE_DIR/.claude" -type f)
while IFS= read -r source; do
  relative=${source#"$CACHE_DIR/skills/"}
  copy_missing "$source" "$DEST/.claude/skills/$relative"
done < <(find "$CACHE_DIR/skills" -type f)
for name in .mcp.json MEMORY.md run.sh; do
  copy_missing "$CACHE_DIR/$name" "$DEST/$name"
done
chmod +x "$DEST/run.sh"

echo "已将 LoopKit 固定提交 $COMMIT 安装到 $DEST"
