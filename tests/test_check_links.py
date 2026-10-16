from pathlib import Path

from check_links import ROOT, find_broken_links, main


def test_detects_broken_link(tmp_path: Path) -> None:
    (tmp_path / "exists.md").write_text("# ok", encoding="utf-8")
    md = tmp_path / "index.md"
    md.write_text(
        "[ok](exists.md) [ng](missing.md) [web](https://example.com) [anchor](#top)",
        encoding="utf-8",
    )
    assert find_broken_links(md) == ["missing.md"]


def test_repository_docs_have_no_broken_links() -> None:
    assert main([str(ROOT / "README.md"), str(ROOT / "docs")]) == 0
