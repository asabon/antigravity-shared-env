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

- **GitHub flow 準拠**: Issue と PR を基盤とした、シンプルで堅牢な標準開発ワークフローを提供します。
- **進捗の保存と復元**: `/save` と `/resume` により、AI が開発コンテキスト（文脈）を維持したまま、いつでも中断・再開が可能です。

### 信頼を支える仕組み (Internal Highlights)
- **2-Step Bootstrap**: `/setup` 一回でプロフェッショナルな AI 開発環境が整います。
- **階層化構成 (Layered Configuration)**: 基盤の更新とプロジェクト固有のカスタマイズを安全に両立します。
- **三重のガード (Triple Guard)**: AI と人の双方が規約を遵守するための多層的なチェック機構。

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
