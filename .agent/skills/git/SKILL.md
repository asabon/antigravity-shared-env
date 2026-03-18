---
name: git
description: このプロジェクト専用の Git 運用ルールに沿った操作（ブランチ作成・コミット）を安全に実行する
---

## 1. ブランチの作成

### 🛠️ 作成手段（第一選択）
原則として **GitHub CLI (`gh`)** を使用してブランチを作成し、Issue と紐付けます。
- **コマンド形式**: `gh issue develop <Issue番号> --name "<Issue番号>-description" --checkout`
- **派生元の最新化**: ブランチを作成する前に、必ず `main` ブランチを最新にしてください（例：`git checkout main; git pull`）。

### 💡 命名規則
- **形式**: `<Issue番号>-<kebab-case-description>` (例: `57-add-validation`)
- **禁止事項**: 全角文字（日本語など）の使用、および一般的な `fix/` や `feat/` 等のプレフィックス。

### 🛡️ 自動検証（Safe Gate）
ブランチ名が作成（チェックアウト）された直後、必ず以下のスクリプトを実行し、合格すること。
`powershell -ExecutionPolicy Bypass -File .agent/skills/git/scripts/verify-branch-name.ps1`

---

## 2. コミットの作成
- **安全確認**:
  - 破壊的操作（commit, push 等）を行う前に、必ず `git branch --show-current` 等で現在のブランチを確認します。
  - `main` や `develop` ブランチでの直接コミットではないことを確認してください。
- **コミットメッセージの形式 (Conventional Commits 準拠)**:
  - **形式**: `<type>: <description>`
  - **Type**: `feat` (機能追加), `fix` (修正), `docs` (ドキュメント), `style` (スタイル), `refactor` (リファクタ), `chore` (雑務), `style` (フォーマット), `test` (テスト) 等
- **言語の統一**:
  - description は**日本語**で、簡潔かつ具体的に記述してください。
- **一括コミットの回避**:
  - 異なる目的を持つ修正は、個別にコミットしてください。
