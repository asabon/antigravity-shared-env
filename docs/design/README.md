# 開発ワークフロー設計書 (Overview)

本リポジトリにおける開発のライフサイクル、AI Skill の役割、およびコンテキスト継続性の設計思想を定義します。

---

## 1. 設計上の重要原則

以下に、ワークフローを支える 5 つの原則をまとめます。

| 原則 | 概要 / 目的 | 運用イメージ / 詳細 |
| :--- | :--- | :--- |
| **⚖️ 1. Dual Source of Truth** | マクロ（全体）とミクロ（タスク）の分離 | ・**Roadmap**: 全体ゴール、進捗管理<br>・**Issue**: 各タスクの詳細仕様、議論の記録 |
| **📂 2. Early Draft PR** | 作業プロセスの透明化・可視化 | 最初の Commit 直後に Draft PR を作成し、ブラックボックス化を防止 |
| **🛠️ 3. Skill-Driven Execution** | 定型作業の自動化 ＆ 思考の柔軟性確保 | 機械的作業は Skill、実装や計画は AI の試行錯誤に分担 |
| **⚡ 4. Local-First Context** | 高速なレスポンス ＆ 確実なバックアップ | 進捗はローカル（`task.md`）で高速管理、適宜 GitHub に保存 |
| **📝 5. Audit Trail** | 指摘対応の履歴・コンテキストの維持 | チャット指示による修正も、必ず PR コメントに足跡を残す |

---

### 💡 補足：Skill-Driven Execution の区分

定型作業（Mechanical）と柔軟な作業（Intelligence）を区分し、安全性を両立します。

| 区分 | 特徴 / 目的 | 具体的な対象 |
| :--- | :--- | :--- |
| **Skill化 (ガードレール)** | バグが許されない、手順の強制が必須な領域 | ・`flow-kickoff` (Preparing)<br>・`flow-wrapup` (Developing完了時)<br>・`/cleanup`<br>・`/dev-pause`, `/dev-start` |
| **AI の自律 (柔軟・試行錯誤)** | チャットのやり取りや臨機応変な実装・デバッグ | ・**PLANNING**: 計画・発案<br>・**DEVELOPING**: 実装ループ |

---

## 🔗 詳細設計

各トピックの詳細なダイアグラム（Mermaid）は以下を参照してください。

- [🚦 **状態遷移 (State Machine)**](./states.md)
  - IDLE / ACTIVE およびフェーズ（Planning等）の遷移図
- [🔄 **シーケンス図 (Sequence Diagrams)**](./sequences.md)
  - 各フェーズにおけるユーザー・AI・GitHubのメッセージフロー
- [⚙️ **詳細実行フロー (Skill Flows)**](./skills.md)
  - `flow-kickoff` や `flow-wrapup` の内部フローチャート
- [📂 **同期対象ファイル一覧 (Sync Targets)**](./sync_targets.md)
  - 初期セットアップおよび継続同期でのファイル管理対象・除外一覧
