# TypeScript 規約 [11_typescript.md]

TypeScript 開発における、型安全性とコード品質を担保するための統一ルールです。

## 1. コーディング規約

- **TypeScript 自己構成**:
  - `tsconfig.json` に従った実装を徹底してください。
  - 基本的に `strict: true` 構成を推奨します。
- **Lint / Format**:
  - `eslint` および `prettier` が導入されている場合、必ずこれらを実行してコード品質を担保してください。
  - コミット前に `npm run lint` や `npm run format` (または相当するコマンド) を実行してください。

## 2. 許可されているコマンド (SafeToAutoRun: true)

- `npm install`, `yarn install`, `pnpm install`
- `npm run build`, `npm run test`, `npm run lint`
- `tsc --noEmit`
- `ls`, `cat`, `dir` (情報取得)

## 3. 実装完了後の必須検証

タスク完了を宣言する前に、以下の項目を確認してください。

1. [ ] ビルドエラーおよび型エラーがないこと
2. [ ] ユニットテストがすべてパスすること
3. [ ] Lint エラーがないこと
