# TypeScript / GitHub Actions 規約 [11_typescript.md]

TypeScript および GitHub Actions (JavaScript/TypeScript 基盤のカスタムアクション) 開発における統一ルールです。

## 1. コーディング規約

- **TypeScript 自己構成**:
  - `tsconfig.json` に従った実装を徹底してください。
  - 基本的に `strict: true` 構成を推奨します。
- **Lint / Format**:
  - `eslint` および `prettier` が導入されている場合、必ずこれらを実行してコード品質を担保してください。
  - コミット前に `npm run lint` や `npm run format` (または相当するコマンド) を実行してください。

## 2. GitHub Actions (Custom Action) 開発

- **metadata**: `action.yml` (または `action.yaml`) のメタデータを最新の状態に保ってください。
- **dist 配布**:
  - `ncc` 等でビルドした成果物をリポジトリに含める構成の場合、ソースコードの修正に合わせて必ずビルドを行い、成果物を更新してください。
- **検証**:
  - `npm test` 等でユニットテストが用意されている場合、必ずパスすることを確認してください。

## 3. 許可されているコマンド (SafeToAutoRun: true)

- `npm install`, `yarn install`, `pnpm install`
- `npm run build`, `npm run test`, `npm run lint`
- `tsc --noEmit`
- `ls`, `cat`, `dir` (情報取得)

## 4. 実装完了後の必須検証

タスク完了を宣言する前に、以下の項目を確認してください。

1. [ ] ビルドエラーおよび型エラーがないこと
2. [ ] ユニットテストがすべてパスすること
3. [ ] Lint エラーがないこと
4. [ ] (成果物配布型の場合) `dist/` 等の成果物が最新であること
