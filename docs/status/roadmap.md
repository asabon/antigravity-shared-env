# antigravity-workflow Roadmap

このファイルは、antigravity-workflow プロジェクトの全体像と進捗を管理するための「唯一の真実 (Source of Truth)」です。

## フェーズ 1: 基盤構築 (Done)
- [x] 基本的なブランチ保護ルールの策定
- [x] コンテキスト保存・再開ワークフロー (`/save`, `/resume`) の実装
- [x] GitHub 連携 (Issue/PR) の標準化

## フェーズ 2: 構成の簡素化 (Current)
- [x] `*_template` 構造の廃止とルートへの集約
- [x] サブモジュールを介さない直接的な管理への移行
- [x] ルールの整合性レビューと修正
- [x] ディレクトリ命名規則の統一と運用ルールの更なる洗練
- [x] `design.md` に基づくコアワークフローの実装
  - [x] `.antigravityrule` の整備（原則・ガードレールのインストール）
  - [x] 状態同期（`/save`, `/resume`）の Skill・Slash Command 化
  - [x] コアスキル（`kickoff-task`, `wrapup-task` 等）の整合性レビュー・修正

## フェーズ 3: 機能拡張と洗練 (Next)
- [ ] 各スタック（Android, TS, Python）向けルールの更なる具体化
- [ ] 共通スクリプト群の充実 (CI/CD ユーティリティなど)
- [ ] ドキュメントの完全な多言語対応 (日本語/英語)
