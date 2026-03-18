---
name: git
description: このプロジェクト専用の Git 運用ルールに沿った操作（ブランチ作成・コミット）を安全に実行する
---

## 1. ブランチの作成と切り替え

### 🛠️ 作成手順（シーケンス）
原則として **GitHub CLI (`gh`)** を使用し、以下の 4 ステップで安全にブランチを作成します。

1. **ブランチ名の決定**: 
   - 規約（後述）に沿ってブランチ名を決定します。
   - ※ 事前準備として、`main` を最新化してください（例：`git checkout main; git pull`）。

2. **自動検証（Safe Gate）**:
   - コマンドを発行する **直前** に、必ず以下のスクリプトを実行し、合格すること。
   - `powershell -ExecutionPolicy Bypass -File .agent/skills/git/scripts/verify-branch-name.ps1 "<作成予定のブランチ名>"`

3. **リモートブランチの作成**:
   - GitHub CLI で Issue と紐付いたブランチを作成します（バグ回避のため `--checkout` は推奨しません）。
   - `gh issue develop <Issue番号> --name "<作成予定のブランチ名>"`

4. **ローカルへのチェックアウト**:
   - `git fetch origin` または `git checkout <作成したブランチ名>` で、ローカルに切り替えます。

---

### 💡 命名規則
- **形式**: `<Issue番号>-<kebab-case-description>` (例: `57-add-validation`)
- **禁止事項**: 全角文字（日本語など）の使用、および一般的な `fix/` や `feat/` 等のプレフィックス。

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
