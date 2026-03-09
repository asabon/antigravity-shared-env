# Antigravity Shared Environment

このリポジトリは、Antigravity（AI エージェント）を活用した開発プロジェクト間で共通して使用する設定、ワークフロー、ルールを管理するための基盤です。

## 概要

本プロジェクトは、開発の標準化を目的とした「すぐに使える」ルールセットを提供します。以前の複雑なテンプレート形式を廃止し、リポジトリをクローンまたはフォークしてそのまま利用、あるいは必要なファイル（`.agent/`, `.antigravityrule` 等）をプロジェクトルートへコピーするだけで導入可能なシンプルな構成に移行しました。

### ディレクトリ構造

```text
プロジェクトルート/
├── .antigravityrule       <-- AI エージェントの動作指針・ルール目次
├── .agent/                <-- AI 向けの規約・ワークフロー定義
│   ├── rules/             <-- 開発規約 (Workflow, Git, GitHub, スタック別)
│   ├── templates/         <-- 初期化用テンプレート (roadmap.md 等)
│   └── workflows/         <-- 自動化コマンド (/save, /resume 等)
├── .github/               <-- 共通の GitHub 設定 (ISSUE_TEMPLATE 等)
├── .hooks/                <-- Git フックの実体 (pre-push 等)
├── docs/99_progress/      <-- 進捗管理 (roadmap.md)
└── scripts/               <-- 環境構築用スクリプト (ラベル設定、フック有効化)
```

## 主要なルールとワークフロー

| パス | 役割 |
| :--- | :--- |
| `.antigravityrule` | エージェントへの最優先指示。日本語対応や目次機能を提供。 |
| `.agent/rules/01_workflow.md` | `roadmap.md` や Issue を使った開発サイクルの定義。 |
| `.agent/rules/02_git.md` | コミットメッセージ規約、ブランチ保護、Git フックの利用。 |
| `.agent/rules/03_github.md` | Issue/PR の書き方、ラベル運用、自動クローズのルール。 |
| `.agent/templates/roadmap.md` | 新規プロジェクト開始時の `roadmap.md` 初期化用テンプレート。 |
| `.agent/workflows/` | `/save`, `/resume`, `/cleanup` 等のコマンド手順書。 |

## 対応技術スタック

以下のスタックに対する標準的な規約（Lint、Test、Build 等の自動実行許可）が含まれています。
- **Android**: Kotlin, Compose, Gradle
- **TypeScript**: GitHub Actions (Custom Action), Node.js
- **Python**: スクレイピング, データ解析, CI

## 使い方
 
 ### 1. 導入
 必要な設定ファイル（`.antigravityrule`, `.agent/`, `.github/` 等）を、対象プロジェクトのルートディレクトリにコピーしてください。
 
 ### 2. 初期セットアップと最適化
 AI エージェントに対して以下のように指示してください。
 
 > 「`.antigravityrule` に基づいて、プロジェクトの初期化（Roadmap のセットアップ）と不要なルールの削除を行って」
 
 これにより、AI は `docs/99_progress/roadmap.md` の作成や、プロジェクトのスタックに合わせた `.antigravityrule` のクリーンアップを自動的に行います。
 
 また、以下のスクリプトを実行して GitHub ラベルとローカルフックを有効化することを推奨します。
```powershell
& ./scripts/setup-labels.ps1
& ./scripts/setup-hooks.ps1
```

## 改善・フィードバック

プロジェクトでの利用中に共通ルールの改善点を見つけた場合は、本リポジトリへの Issue 作成やプルリクエスト (PR) を通じて還元してください。
**`main` ブランチへの直接プッシュは禁止されています。**
