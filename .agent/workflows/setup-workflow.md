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
     - `git checkout upstream-bootstrap/main -- .antigravityrule .agent/ .hooks/ scripts/ ":(exclude).agent/custom/*"`
   - 同期完了後、リモートを削除してください： `git remote remove upstream-bootstrap`

2. **ロードマップの初期化**
   - `docs/status/roadmap.md` の内容がプレースホルダー（例: `# [Project Name] Roadmap`）の場合、またはファイルが存在しない場合は、`.agent/templates/roadmap.md` をベースにして新しく作成してください。

3. **技術スタックの特定と規約の準備**
   - プロジェクトの主要ファイルから技術スタック（Android, Next.js, Python 等）を特定してください。
   - **階層化構成の初期化**:
     - `.agent/custom/` ディレクトリを作成し、基盤の `README.md` をコピーしてください。
     - 特定したスタックに応じた固有規約を `.agent/custom/` 配下に作成し、ユーザーに提案してください。

4. **テンプレート固有ファイルのクリーンアップ**
   - ルートの `README.md` を現在のプロジェクト向けに書き換えてください。
   - 不要な `CONTRIBUTING.md` および `LICENSE`（テンプレート固有のもの）を削除してください。

5. **環境構築スクリプトの実行**
   - 以下のスクリプトを実行して、GitHub ラベルと Git フックを有効化してください。
     - `./scripts/windows/setup-labels.ps1`
     - `./scripts/windows/setup-hooks.ps1`

6. **セットアップ完了の報告**
   - 作成・更新したファイルの一覧を報告し、ロードマップに基づく開発の開始を案内してください。
