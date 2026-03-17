---
name: github-pr
description: このプロジェクト専用の PR 運用ルールに沿った操作（Draft作成・本文更新・最終化）を安全に実行する
---

## 1. Draft PR の作成
- **タイトルの検証**:
  - タイトルに `feat:`, `fix:` 等の接頭辞（プレフィックス）が含まれていないこと、および**日本語**であることを確認します。
- **テンプレートの遵守**:
  - `.github/pull_request_template.md` の構成に必ず従い、全ての必須項目を適切に埋めます。
- **関連 Issue の紐付け**:
  - 本文（Description）に `Closes #<Issue番号>` を含め、関連付けされていることを確認します。
- **安全な作成（Draft 強制）**:
  - コマンド実行時は、必ず `--draft` オプション（`gh pr create --draft`）を使用します。
  - 文字化けやエスケープミスを防ぐため、長文になる場合は一時ファイルを生成し、`--body-file` で指定して実行します。

- **ラベルの付与**:
  - 作成時に必ず適切な **「分類ラベル」** を付与してください。
  - *代表例*: `enhancement` (機能追加), `bug` (バグ修正), `chore` (雑務), `documentation`
- **リリース制御ラベル**:
  - 必要に応じて、1つの PR に対して以下のうち**最大1つまで**を付与できます（重複禁止）。
  - *種類*: `major`, `minor`, `breaking`
  - *詳細な一覧*: [03_github.md](../../rules/03_github.md) のセクション5 を参照してください。

---

## 2. PR の更新（本文編集）
- **安全な編集**:
  - 本文を更新（Edit）する際、特に長文になる場合は一時ファイルを生成し、`gh pr edit <PR番号> --body-file <ファイル名>` で実行することを**強く推奨**します（文字化け・事故防止）。

---

## 3. PR を Ready for review にする (最終化)
- **絶対条件**: 以下のコマンドを実行し、自動検証に合格（**`[RESULT] Verification PASSED!`**）することを確認します。
  `powershell -ExecutionPolicy Bypass -File .agent/skills/github-pr/scripts/verify-pr.ps1 -PrNumber <PR番号>`
  ※ 合格しない限り、次のステップに進んで不具合の修正を行ってください。
- **実行**: `gh pr ready <PR番号>` を実行し、Draft 状態を解除（Ready）します。

> [!CAUTION]
> **完了報告の絶対条件ガード (Safe Gate)**
> 上記の自動検証が「PASSED」になり、且つ PR が `Ready for review`（Draft 解除済み）になるまでは、**決して `notify_user`（完了報告）を実行してはなりません**。

- **自律的な表示確認**:
  - `gh pr view <PR番号> --web` 等を利用し、表示崩れ等がないか目視確認（自律確認）することを推奨します。
