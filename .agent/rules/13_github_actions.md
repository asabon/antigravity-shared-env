# GitHub Actions 規約 [13_github_actions.md]

GitHub Actions (ワークフローおよび JavaScript/TypeScript 基盤のカスタムアクション) 開発における統一ルールです。

## 1. GitHub Actions (Custom Action) 開発

- **metadata**: `action.yml` (または `action.yaml`) のメタデータを最新の状態に保ってください。
- **dist 配布**:
  - `ncc` 等でビルドした成果物をリポジトリに含める構成の場合、ソースコードの修正に合わせて必ずビルドを行い、成果物を更新してください。
- **検証**:
  - `npm test` 等でユニットテストが用意されている場合、必ずパスすることを確認してください。

## 2. ワークフロー定義

- **セキュリティ**: `secrets` の扱い、および `permissions` 設定を最小権限の原則 (Least Privilege) に基づいて構成してください。
- **再利用性**: 共通処理がある場合は、Composite Action や Reusable Workflow の活用を検討してください。

## 3. 許可されているコマンド (SafeToAutoRun: true)

- `gh` コマンド全般 (PR, Issue, Workflow 操作)
- `ls`, `cat`, `dir` (情報取得)

## 4. 実装完了後の必須検証

タスク完了を宣言する前に、以下の項目を確認してください。

1. [ ] `action.yml` の定義とソースコードに不整合がないこと
2. [ ] (成果物配布型の場合) `dist/` 等の成果物が最新であること
3. [ ] ユニットテストがすべてパスすること
4. [ ] ワークフローの YAML シンタックスエラーがないこと
