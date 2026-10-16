# YouTube運用・動画作成チーム ドキュメント

YouTubeチャンネルの運用および動画制作を行うチームの運営ドキュメントです。
役割分担、制作フロー、チェックリスト、各種テンプレートをまとめています。

## 目次

- [チーム構成・役割分担](docs/team-roles.md)
- [動画制作ワークフロー](docs/workflow.md)
- [チェックリスト](docs/checklists.md)
- [必要なアプリ・資機材リスト](docs/equipment-and-tools.md)
- [市場分析:企画別](docs/market-analysis.md)
- [初期構成・投稿プラン](docs/posting-plan.md)
- テンプレート
  - [企画書テンプレート](docs/templates/video-planning-template.md)
  - [台本テンプレート](docs/templates/script-template.md)

## 運用の基本方針

- 企画から公開までの各工程で担当者と完了基準を明確にする
- 公開前は必ずチェックリストで最終確認を行う
- 企画書・台本はテンプレートに沿って作成し、情報の抜け漏れを防ぐ

## Python 利用環境

補助スクリプトは Python(3.11 以上、推奨 3.13)で動作します。パッケージ管理には [uv](https://docs.astral.sh/uv/) を使用します。

```bash
# uv のインストール(未導入の場合)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 仮想環境(.venv)の作成と依存関係のインストール
uv sync

# テスト・Lint・フォーマット
uv run pytest
uv run ruff check .
uv run ruff format .

# docs 内の相対リンク切れチェック
uv run python scripts/check_links.py
```

- ライブラリを追加する場合: `uv add <パッケージ名>`(開発用は `uv add --dev <パッケージ名>`)
- スクリプトは `scripts/`、テストは `tests/` に配置します
- Claude Code のクラウドセッションでは、開始時に `.claude/hooks/session-start.sh` が `uv sync` を自動実行します
