# 開発ワークフロー設計書 (Development Workflow Design)

本リポジトリにおける開発のライフサイクル、AI Skill の役割、およびコンテキスト継続性の設計思想を定義します。

## 1. 全体ライフサイクル (Lifecycle Overview)

開発の開始から完了、クリーンアップまでの概要シーケンスです。

```mermaid
sequenceDiagram
    participant U as ユーザー (User)
    participant A as AI Agent (Assistant)
    participant S as AI Skills (手順書)
    participant E as 開発環境 (Issue/Branch/PR)

    U->>A: 開発依頼 (Request)
    
    rect rgb(235, 245, 255)
        Note over A,S: 1. 準備・着手フェーズ (Kickoff)
        A->>S: kickoff-task 読込・実行
        S-->>E: 作業環境の構築 (Issue/Branch/Draft PR)
    end

    rect rgb(240, 240, 240)
        Note over U,E: 2. 実装フェーズ (Implementation)
        loop 実装・試行錯誤
            A->>E: 実装・テスト・Push
            U->>E: 経過確認 (Draft PR)
            U-->>A: フィードバック / /save
        end
    end
    
    rect rgb(235, 255, 235)
        Note over A,S: 3. 完了・最終化フェーズ (Wrapup)
        Note over A: 実装完了の自己判断
        A->>S: wrapup-task 読込・実行
        S-->>E: 成果物の最終化 (Roadmap更新/PR Ready)
        A->>U: 完了報告 (notify_user)
    end

    rect rgb(255, 245, 235)
        Note over U,E: 4. レビュー・マージフェーズ (Review & Merge)
        U->>E: PR レビュー / フィードバック
        alt 修正が必要な場合
            U->>A: 修正依頼
            A->>E: 修正対応 (実装フェーズへ戻る)
        else 承認 (Approved)
            U->>E: マージ (Merge)
        end
    end
    
    U->>E: 5. 収束フェーズ (Cleanup)
    U->>E: /cleanup によるブランチ整理
```

## 2. 着手フロー (Kickoff Flow)

`kickoff-task` Skill が担う、作業開始時の詳細な論理フローです。

```mermaid
flowchart TD
    Start([開発依頼の受領]) --> DecideKickoff[着手が必要か判断]
    DecideKickoff --> ReadSkill[kickoff-task 読込]
    ReadSkill --> ReadRoadmap[Roadmap読込]
    ReadRoadmap --> IdentifyIssue{Issue特定}
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

`wrapup-task` Skill が担う、品質確保と最終化の詳細なフローです。

```mermaid
flowchart TD
    Complete([実装完了の判断]) --> ReadSkill[wrapup-task 読込]
    ReadSkill --> Validation[最終動作検証]
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
