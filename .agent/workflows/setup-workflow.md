---
description: プロジェクトの初期設定を行い、最新のワークフローをインストールします
---
このコマンドは、テンプレートから新しく作成されたプロジェクトを「最新の Antigravity 環境」へブートストラップ（起動）し、初期セットアップを行うためのコマンドです。

AIエージェントは、以下の手順で現在のプロジェクトの初期化を行ってください。

1. **最新基盤の取得 (Bootstrap)**
   - 最新の共通規約やワークフローを反映するため、一時的なリモートを登録して同期を行います。
   - **前提条件**: `git status` を確認し、未コミットの変更がない（ワーキングツリーがクリーンである）ことを確認してください。
   - `git remote add upstream-bootstrap https://github.com/asabon/antigravity-workflow.git`
   - `git fetch upstream-bootstrap main`
   - **Core ファイルの強制同期**: 履歴を無視して最新のファイルのみを取得・上書きします。
     - `git checkout upstream-bootstrap/main -- .antigravityrule .agent/ .hooks/ scripts/ .github/ .vscode/settings.json .gitignore ":(exclude).agent/custom/*" .agent/custom/README.md docs/workflow/ docs/design/`
   - 同期完了後、リモートを削除してください： `git remote remove upstream-bootstrap`

2. **ロードマップの初期化**
   - `docs/status/roadmap.md` の初期化時、`.agent/templates/` 配下にある複数のテンプレートからプロジェクトの進め方に応じたものを**ユーザーに提示し、選択してもらってから**作成してください。
     - `roadmap_phase.md`: 段階的な成長・マイルストーン重視型
     - `roadmap_now_next_later.md`: アジャイル・優先順位重視型
     - `roadmap_feature.md`: 機能・コンポーネントベース型
   - 既存の `docs/status/roadmap.md` がプレースホルダーの場合、または存在しない場合にこの処理を行います。

3. **階層化構成の初期化 (Custom Rules)**
   - 説明用 `.agent/custom/README.md` が適切に配備されていることを確認してください。
   - ユーザーに対し、現在使用している技術スタック（Android, Python 等）に応じた固有の規約がある場合は、このディレクトリ内へファイルを追加することを提案してください。

4. **テンプレート固有ファイルのクリーンアップ**
   - ルートの `README.md` を現在のプロジェクト向けに書き換えてください。
   - 不要な `CONTRIBUTING.md` および `LICENSE`（テンプレート固有のもの）を削除してください。

5. **環境構築スクリプトの実行**
   - 以下のスクリプトを実行して、GitHub ラベルと Git フックを有効化してください。
     - `./scripts/windows/setup-labels.ps1`
     - `./scripts/windows/setup-hooks.ps1`

6. **セットアップ完了の報告**
   - 作成・更新したファイルの一覧を報告し、ロードマップに基づく開発の開始を案内してください。
