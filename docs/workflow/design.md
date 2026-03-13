# 開発ワークフロー設計書 (Development Workflow Design)

本リポジトリにおける開発のライフサイクル、AI Skill の役割、およびコンテキスト継続性の設計思想を定義します。

## 1. 全体ライフサイクル (Lifecycle Overview)

開発の開始から完了、クリーンアップまでのシーケンスです。

```mermaid
sequenceDiagram
    participant U as ユーザー (User)
    participant R as roadmap.md
    participant I as GitHub Issue
    participant S as AI Skill (kickoff/wrapup)
    participant B as 作業ブランチ
    participant P as Pull Request

    U->>R: 内容確認
    U->>S: /kickoff (または作業開始)
    S->>I: Issue特定・同期
    S->>B: ブランチ作成 & チェックアウト
    S->>P: Draft PR作成 (早期公開)
    
    Note over B,P: 実装フェーズ (CI/CD, 検証)
    
    U->>S: /wrapup (または作業完了)
    S->>R: 完了マーク付与
    S->>P: Ready for review
    U->>P: マージ (Merge)
    U->>B: /cleanup (ブランチ削除)
```

## 2. 着手フロー (Kickoff Flow)

`kickoff-task` Skill が担う、作業開始時の論理フローです。

```mermaid
flowchart TD
    Start([作業開始]) --> ReadRoadmap[Roadmap読込]
    IdentifyIssue{Issue特定}
    IdentifyIssue -- 既存なし --> CreateIssue[Issue作成]
    IdentifyIssue -- 既存あり --> SyncIssue[Issue同期]
    CreateIssue --> CreateBranch[ブランチ作成 & チェックアウト]
    SyncIssue --> CreateBranch
    CreateBranch --> UpdateRoadmap[Roadmapを着手中へ]
    UpdateRoadmap --> InitTaskMD[task.md 初期化]
    InitTaskMD --> DraftPR[Draft PR作成]
    DraftPR --> End([準備完了])
```

## 3. 完了フロー (Wrapup Flow)

`wrapup-task` Skill が担う、品質確保と最終化のフローです。

```mermaid
flowchart TD
    Complete([実装完了]) --> Validation[最終動作検証]
    Validation --> UpdateRoadmap[Roadmapを完了へ]
    UpdateRoadmap --> CommitPush[Commit & Push]
    CommitPush --> ReadyPR[gh pr ready]
    ReadyPR --> Report[完了報告]
    Report --> End([レビュー待ち])
```

## 4. コンテキスト継続性 (Context Persistence)

`/save` と `/resume` による、中断・再開のステート管理です。

```mermaid
stateDiagram-v2
    [*] --> Coding: 着手
    Coding --> Saving: /save 実行
    Saving --> Checkpoint: Issueへ記録
    Checkpoint --> Idle: 中断
    Idle --> Resuming: /resume 実行
    Resuming --> Coding: コンテキスト復元
    Coding --> [*]: マージ・完了
```

## 5. 設計上の重要原則

1. **GitHub Issue as the Source of Truth**: 設計判断やタスクリストの詳細は常に Issue に集約され、AI の `task.md` はその一時的な写しに過ぎません。
2. **Early Draft PR**: コードの透明性を保つため、最初の Commit 直後に Draft PR を作成します。
3. **Skill-Driven Execution**: 複雑な手順は Skill (`SKILL.md`) にカプセル化し、実行時の安定性を担保します。
