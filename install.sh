#!/usr/bin/env bash
# install.sh: Install text_fancipy in editable mode
# text_fancipy: Convert plain ASCII text to fancy Unicode text styles

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Installing text_fancipy (editable) ==="
uv pip install -e .
echo "=== Install complete ==="
