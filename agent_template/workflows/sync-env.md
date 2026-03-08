---
description: 共通リポジトリ (env/) から現在のリポジトリに最適なルールや設定を選択・展開し、不要なものを削除する（引き算方式）
---
# 共通環境同期ワークフロー (sync-env)

このワークフローは、`env/` 内のテンプレートから必要なアセットを取り込み、プロジェクトに合わせて最適化（不要なものの削除）を行います。

## 手順

### 1. プロジェクト分析
- `env/README.md` を読み、提供されているアセットの全体像を把握してください。
- 現在のリポジトリの構造、主要言語、既存の `.antigravityrule` や `.github/` ディレクトリの内容を分析し、以下のいずれのスタックに該当するか（または複数か）を特定してください。
    - **Android**: Kotlin, Compose, Gradle 等がある場合
    - **TypeScript**: `package.json`, `tsconfig.json`, `action.yml` 等がある場合
    - **Python**: `.py` ファイル、`requirements.txt`, `pytest` 等がある場合

### 2. テンプレートの展開とリネーム (Safety Rename)
特定したスタックに基づき、以下のファイルをプロジェクトルートに展開してください。**展開時、必ずドット付きの正しい名前にリネームしてください。**

- **アンカー設定**:
    - `env/antigravityrule.template` -> `./.antigravityrule`
- **AI ルール**:
    - `env/agent_template/` 内の全ファイルを `./.agent/` ディレクトリにコピーしてください。
- **GitHub ワークフロー**:
    - `env/github_template/workflows/` 内の共通ファイルを実行ディレクトリ `./.github/workflows/` にコピーしてください。
    - 特定されたスタックに応じたテンプレート（`env/github_template/workflows/template-<stack>/` 内）を `./.github/workflows/` にコピーしてください。
- **Git フック & スクリプト**:
    - `env/hooks_template/` -> `./.hooks/`
    - `env/scripts_template/` -> `./scripts/`

### 3. ルールの最適化（引き算）
コピー完了後、直ちに以下の最適化を実行してください。

1. **`.antigravityrule` のクリーンアップ**:
   - ステップ 1 で特定した技術スタック**以外**のインデックス（[Android], [TypeScript], [Python] セクション）を、ファイル内から完全に削除してください。
   - `rules:` リスト内からも、存在しないファイルの項目を削除してください。
2. **ルールの整理**:
   - `./.agent/rules/` 内にコピーされたファイルのうち、プロジェクトに関係のない番号付きファイルを削除してください（例: Android 以外なら `10_android.md` を削除）。
3. **ワークフローの整理**:
   - 不要な GitHub Actions ワークフローが混入している場合は削除してください。

### 4. ユーザー確認
- 展開・削除したファイルの一覧をユーザーに報告し、完了したことを伝えてください。
- 必要に応じて、`setup-labels` や `setup-hooks` スクリプトの実行を提案してください。
