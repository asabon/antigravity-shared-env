# Antigravity Shared Environment

このリポジトリは、Antigravity（AI エージェント）を活用した開発プロジェクト間で共通して使用する設定、ワークフロー、ルールをまとめたものです。

安全のため、各設定ファイルは `.template` 拡張子や `_template` ディレクトリ名で管理されており、AI が誤ってルールとして直接認識しないよう配慮されています。

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

## 使い方（同期の手順）

1. ターゲットプロジェクトのルートでこのリポジトリを Submodule として追加します。
   ```bash
   git submodule add https://github.com/asabon/antigravity-shared-env.git env
   ```
2. AI エージェントに対して以下のように指示し、環境を同期させます。
   ```
   /sync-env
   ```
   または「`env/agent_template/workflows/sync-env.md` を実行して同期して」と指示してください。

3. **AI による「引き算」同期**:
   AI がプロジェクトを分析し、必要なテンプレートをリネーム（ドット付きに修正）してルートに展開した後、不要なセクションを削除して最適化します。