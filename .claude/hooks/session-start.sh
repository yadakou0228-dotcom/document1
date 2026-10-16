#!/bin/bash
# クラウドセッション開始時に Python 環境(uv)を同期する
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
uv sync
