# Git 運用ルール

このプロジェクトでエージェントが Git 操作を行う際の統一ルールです。

## 1. コミットメッセージ
- **形式**: [Conventional Commits](https://www.conventionalcommits.org/) (`<type>: <description>`)
- **Type**: `feat`, `fix`, `docs`, `refactor`, `chore` など
- **言語**: description は**日本語**で、簡潔かつ具体的に記述してください。
- **注意**: コミットメッセージにはプレフィックスを付けますが、最終的なリリースノートには **PR タイトル** が使用されます。[GitHub 運用ルール](./03_github.md#3-pull-request-pr-の作成) との違いに注意してください。

## 2. コミットの粒度
- 1つのコミットには、1つの論理的な変更のみを含めてください。
- 異なる目的を持つ修正は、個別にコミットしてください。

## 3. ブランチ作成
- 新しいタスクを開始する際は、必ず **`main` ブランチを最新にしてから、`main` から作業用ブランチを派生**させてください。
- GitHub Issue 番号を付与したブランチを作成してください。
- **推奨手順**: GitHub CLI (`gh issue develop`) を使用してブランチを作成すると、GitHub 上で Issue とブランチが直接紐付けられます。
  - **重要**: `--name` オプションには、必ず **"Issue番号-説明"** の形式を指定してください。
  - **コマンド例**: `gh issue develop <Issue番号> --name "<Issue番号>-kebab-case-description" --checkout`
- **命名規則**: `<Issue番号>-<kebab-case-description>`
- **アンチパターン**: `gh issue develop 17 --name "refactor-agent"` とすると、ブランチ名が `refactor-agent` になり番号が抜けるため**NG**です。
- **事前チェック**: 破壊的操作 (commit, push) を行う前に、必ず `git branch --show-current` 等で現在作業中のブランチが意図通りであることを指差し確認してください。

- **禁止事項**: 以下の行為は厳禁です。
  - **`main` ブランチへの直接 push**: すべての変更(ドキュメント修正を含む)は必ず作業ブランチを作成し、PR を経由してください。
  - **ブランチ名への日本語(全角文字)の使用**: 必ず英語(小文字のケバブケース)を使用してください。
    - **正**: `9-implement-discount-calculator`
    - **誤**: `9-割引計算機能の実装`

## 4. 物理的なブランチ保護 (Git Hooks)

プロジェクトの整合性と `main` ブランチの品質を担保するため、`.hooks/` に定義された Git Hooks を活用した「物理的なガードレール」を導入しています。

### 運用ポリシー
- **トピックブランチの強制**: すべての開発・修正作業は `main` ブランチから分岐したトピックブランチ（Issue 番号付き）で行う必要があります。
- **PR 経由の統合**: `main` ブランチへの変更取り込みは、必ず Pull Request のレビューとマレ方式（Merge）を経て行われる必要があります。直接的な操作（コミットやプッシュ）は、誤操作であってもシステム的に阻止します。

### セットアップ手順
開発を開始する前に、以下のスクリプトを実行してフックを有効化してください。
- **Windows**: `./scripts/win/setup-hooks.ps1`
- **Linux/macOS**: `./scripts/linux/setup-hooks.sh`

※内部的には `git config core.hooksPath .hooks` を実行しています。

### フックの詳細
- **[pre-commit](file:///e:/work/antigravity-shared-env/.hooks/pre-commit)**:
  - コミット実行時に現在のブランチ名を確認します。
  - `main` ブランチでのコミットを検知した場合、エラーメッセージを表示してコミットを中断させます。
- **[pre-push](file:///e:/work/antigravity-shared-env/.hooks/pre-push)**:
  - プッシュ実行時に現在のブランチ名を確認します。
  - `main` ブランチからのプッシュを検知した場合、エラーメッセージを表示してプッシュを中断させます。
  - これにより、リモートの `main` ブランチが誤って上書きされるリスクを物理的に排除します。

## 5. 実行権限と承認

### 許可が必要な操作 (SafeToAutoRun: false)
以下の破壊的または共有を伴う操作は、必ずユーザーの明示的な許可を得てから実行してください。
- `git commit`
- `git push`
- `git pull`
- `git branch -d / -D`

### 許可なしで実行可能な操作
自動実行が許可されているコマンド（SafeToAutoRun: true）の最新リストについては、対象とするプラットフォームに関わらず、**`.vscode/settings.json` 内の `chat.tools.terminal.autoApprove` を参照・遵守**してください。

**【自律的操作における制約事項】**
- `git add`: インデックスへの追加（ステージング）のみ許可されます。コミットやプッシュは必ずユーザーの承認を得る必要があります。
- `git checkout`: 既存ブランチへの切り替え、または `gh issue develop` 等の規約に付随する作業ブランチ作成のみ許可されます。
