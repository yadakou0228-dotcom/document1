"""Markdown内の相対リンク切れを検出するスクリプト。

使い方:
    uv run python scripts/check_links.py [対象ディレクトリ ...]

引数を省略した場合はリポジトリ直下の README.md と docs/ 以下を検査する。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.suffix == ".md":
            files.append(p)
    return files


def find_broken_links(md_file: Path) -> list[str]:
    broken: list[str] = []
    for target in LINK_RE.findall(md_file.read_text(encoding="utf-8")):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue  # 外部URL・mailto・ページ内アンカーは対象外
        path = target.split("#", 1)[0]
        if path and not (md_file.parent / path).exists():
            broken.append(target)
    return broken


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv] or [ROOT / "README.md", ROOT / "docs"]
    errors = 0
    for md in iter_markdown(targets):
        for link in find_broken_links(md):
            print(f"{md}: リンク切れ -> {link}")
            errors += 1
    print("OK: リンク切れはありません" if errors == 0 else f"NG: {errors} 件のリンク切れ")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
