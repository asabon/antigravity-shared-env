# Antigravity Shared Environment

このリポジトリは、Antigravity（AI エージェント）を活用した開発プロジェクト間で共通して使用する設定、ワークフロー、ルールをまとめたものです。

安全のため、各設定ファイルは `.template` 拡張子や `_template` ディレクトリ名で管理されており、AI が誤ってルールとして直接認識しないよう配慮されています。

## 概要（推奨される構成）

このリポジトリは、ターゲットとなるプロジェクトのルート直下に **`env/`** という名前のディレクトリを作成し、その中に `git submodule` または `git clone` して配置して使用することを推奨しています。

```text
プロジェクトルート/
├── env/                <-- ここにこのリポジトリを配置
│   ├── README.md
│   ├── antigravityrule.template
│   └── ...
├── .antigravityrule    <-- 同期によって生成される
└── .agent/             <-- 同期によって生成される
```

`env/` ディレクトリ内に「共有済みの本来の設定」を隔離しておくことで、プロジェクト本体の設定（ドット付きファイル）と明確に区別でき、AI による誤認識を防ぎつつ、いつでもクリーンな状態から共通設定を再展開できるようになります。

## ディレクトリ構成と役割

- **`antigravityrule.template`**
  - AI エージェントの動作指針。Android, TypeScript, Python のインデックスを含みます。
- **`agent_template/`**
  - **`rules/`**: 共通（01-03）および技術スタック別（10-12）のルール定義。
  - **`workflows/`**: `/save`, `/resume`, `/cleanup`, `/sync-env` コマンド定義。
- **`github_template/`**
  - GitHub Actions のワークフロー（共通、およびスタック別テンプレート）。
- **`hooks_template/`**
  - ローカル開発用の Git フック (`pre-commit`, `pre-push`)。
- **`scripts_template/`**
  - GitHub ラベルの自動セットアップやフック有効化スクリプト。

## 対応技術スタック
- **Android**: Kotlin, Compose, Gradle, Android CI/CD
- **TypeScript / GitHub Actions**: カスタムアクション開発、JavaScript/Node.js 基盤
- **Python / Scraping**: スクレイピング、DB構築、CI での自動実行

## 使い方（新規プロジェクトへの導入手順）

新しいリポジトリでこれらの共通ルールを適用する手順です。

1. **Submodule の追加**
   プロジェクトのルートで以下を実行します。
   ```bash
   git submodule add https://github.com/asabon/antigravity-shared-env.git env
   ```

2. **初期同期の実行 (Initial Sync)**
   この時点ではまだプロジェクト側に `/sync-env` コマンドが存在しません。AI エージェントに対し、**Submodule 内のファイルを直接指定して実行**するよう指示してください。
   
   **指示の例:**
   > 「`env/agent_template/workflows/sync-env.md` を実行して、環境の同期を開始して」

3. **AI による「引き算」同期の自動実行**
   指示を受けた AI がプロジェクトを分析し、以下の処理を自動で行います。
   - 必要なテンプレートをリネーム（ドット付きに修正）してプロジェクトルートに展開
   - 二回目以降のために `/sync-env` スラッシュコマンドを `.agent/workflows/` に配置
   - プロジェクト構成を判定し、`.antigravityrule` 等から不要なスタックの記述を削除して最適化

同期完了後は、通常通り `/sync-env` コマンドでいつでも最新の共通設定にアップデートできるようになります。