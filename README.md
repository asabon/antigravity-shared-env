# antigravity-workflow

このリポジトリは、AI エージェント Antigravity が GitHub 上で自律的に開発タスクを実行するための標準ワークフローと設定を定義する基盤リポジトリです。

---

## 使い方 (Usage)

導入は以下の **2 ステップ** で完了します。

### ステップ 1: 初期導入 (Setup)
新しいプロジェクトを開始する際に、本リポジトリの [.agent/workflows/setup-workflow.md](.agent/workflows/setup-workflow.md) を対象プロジェクトにコピーし、AI エージェントに以下を指示してください。
> `/setup` を実行してプロジェクトを初期化してください。

**この操作により、最新の共通規約、ワークフロー、および環境構築スクリプトが自動的にプロジェクトへインストールされます。**

### ステップ 2: 継続更新 (Sync)
導入後は、インストールされた `/sync-workflow` を定期的に実行するだけで、本リポジトリで改善された最新のワークフローを反映できます。
> `/sync-workflow`

---

## 主な特徴 (Key Features)

- **2-Step Bootstrap**: `/setup` 一回で最新の AI 開発環境が整います。
- **階層化構成 (Layered Configuration)**: 
  - 基盤ルール (`.agent/rules/`) と、プロジェクト固有ルール (`.agent/custom/`) を分離。
  - プロジェクト側のカスタマイズを破壊せずに基盤のみをアップデート可能です。
- **進捗の保存・復元**: `/save`, `/resume` による開発コンテキストの維持。
- **三重のガード (Triple Guard)**: PR の最終化や規約遵守を AI と人の双方に徹底させる仕組み。

---

## ディレクトリ構造 (Structure)

```text
├── .antigravityrule       <-- AI エージェントの動作指針・ルール目次
├── .agent/                <-- AI 向けの規約・ワークフロー定義
│   ├── rules/             <-- 共通規約 (同期対象)
│   ├── custom/            <-- プロジェクト固有規約 (同期対象外)
│   ├── templates/         <-- 初期化用テンプレート
│   └── workflows/         <-- 自動化コマンド (/save, /setup-workflow, /sync-workflow 等)
├── .github/               <-- 共通の GitHub 設定
├── .vscode/               <-- VS Code 設定
├── docs/status/           <-- 進捗管理 (roadmap.md)
└── scripts/               <-- 環境構築用スクリプト
```

---

## フィードバックと還元 (Contributing)

優れたワークフローの改善案を発見した場合は、ぜひ本リポジトリへフィードバックしてください。詳細は [CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください。
