# Antigravity Shared Environment

このリポジトリは、Antigravity（AI エージェント）を活用した開発プロジェクト間で共通して使用する設定、ワークフロー、ルールをまとめたものです。

安全のため、各設定ファイルは `.template` 拡張子や `_template` ディレクトリ名で管理されており、AI が誤ってルールとして直接認識しないよう配慮されています。

## 概要（推奨される構成）

このリポジトリは、ターゲットとなるプロジェクトのルート直下に **`env/`** という名前のディレクトリを配置（`git submodule` 推奨）して使用します。
AI エージェントが `/sync-env` コマンドを実行することで、`env/` 内のテンプレートが必要な形にリネームされ、プロジェクト直下へ展開されます。

```text
プロジェクトルート/
├── env/                   <-- このリポジトリ (ReadOnly 推奨)
│   ├── antigravityrule.template
│   ├── agent_template/
│   └── ...
├── .antigravityrule       <-- [生成] プロジェクトの目次
├── .agent/                <-- [生成] AI 向けの命令・ワークフロー
│   ├── rules/
│   └── workflows/
├── .github/               <-- [生成] CI/CD 設定
│   └── workflows/
├── .hooks/                <-- [生成] Git Hooks
└── scripts/               <-- [生成] 便利スクリプト
```

## 同期の実態（ファイルマッピング）

`/sync-env` を実行すると、AI は `env/` 内のテンプレートを以下のようにプロジェクトルートへ展開し、必要に応じてリネーム（ドットの付与など）を行います。

| 同期元 (env/ 内) | 同期先 (プロジェクトルート) | 役割 |
| :--- | :--- | :--- |
| `antigravityrule.template` | `.antigravityrule` | AI エージェントのメイン動作指針・目次 |
| `agent_template/rules/` | `.agent/rules/` | 開発規約、フェーズ別ルール定義 |
| `agent_template/workflows/` | `.agent/workflows/` | `/save`, `/resume`, `/sync-env` などのコマンド定義 |
| `github_template/workflows/` | `.github/workflows/` | GitHub Actions の自動化パイプライン |
| `hooks_template/` | `.hooks/` | `pre-commit` などのローカル Git フック |
| `scripts_template/` | `scripts/` | ラベル設定やフック有効化の自動実行スクリプト |

## 対応技術スタック

本環境は、以下のスタックを標準サポートしています。

- **Android**: Kotlin, Compose, Gradle, Android CI/CD
- **TypeScript**: GitHub Actions (Custom Action), JavaScript/Node.js
- **Python**: スクレイピング, データ解析, CI 自動実行

## 使い方（導入手順）

### 1. Submodule の追加
プロジェクトのルートで以下を実行します。
```bash
git submodule add https://github.com/asabon/antigravity-shared-env.git env
```

### 2. 初期同期の指示
初めて導入する際は、AI に対して以下のように「同期ワークフローの直接実行」を指示してください。

> 「`env/agent_template/workflows/sync-env.md` を実行して、環境の同期を開始して」

### 3. AI による「引き算」と最適化
指示を受けた AI は、プロジェクトの構成を自動で分析し、以下の最適化を行います。

- **不要ルールの削除**: プロジェクトが Python を使っていない場合、`.antigravityrule` から Python 関連のインデックスを削除し、`.agent/rules/` から Python 用のルールファイルを削除します。
- **CI/CD の選択**: プロジェクトの種類にマッチする GitHub Actions テンプレートのみを `.github/workflows/` に配置します。
- **プロジェクト固有情報の維持**: すでにプロジェクト側に独自のルールや設定がある場合、それらを壊さないように配慮しながら共通設定を統合します。

同期完了後は、プロジェクトルートに配置された `/sync-env` コマンドで、いつでも最新の共通設定にアップデートできるようになります。

## 改善・フィードバックの提案

プロジェクトでの利用中に共通ルールの改善点を見つけた場合は、以下の手順でフィードバックしてください。

1. **Issue の作成**: 本リポジトリ (`antigravity-shared-env`) に Issue を作成してください。
2. **プルリクエスト (PR)**: 改善案のブランチを作成し、PR を出してください。**`main` ブランチへの直接プッシュは禁止されています。**
3. **AI による提案**: AI が「これは共通化すべき」と判断した場合、本リポジトリへの Issue 作成を提案することがあります。
