# 詳細実行フロー (Skill Flows)

エージェントが各オーケストレーター（自動化 Skill）を実行する際の内訳・チェックフローのマシナリーを定義します。

---

## 1. 着手フロー (Kickoff Flow)

`flow-kickoff` Skill 等が担う、作業開始時の詳細な論理手順です。

```mermaid
flowchart TD
    Start([開発依頼・セッション開始]) --> ReviewPlan["💡 計画(Planning): 計画の確認"]
    ReviewPlan --> ProposeIssue["次の一手の提案"]
    ProposeIssue --> SelectIssue{"ユーザーによる選択"}
    SelectIssue --> SyncIssue["Issueの確定・起票"]
    
    SyncIssue --> ReadSkill["💡 準備(Preparing): flow-kickoff 等の開始"]
    
    ReadSkill --> CreateBranch["ブランチ作成 ＆ チェックアウト"]
    CreateBranch --> UpdateRoadmap["Roadmapを着手中へ"]
    UpdateRoadmap --> InitTaskMD["task.md 初期化"]
    InitTaskMD --> DraftPR["Draft PR作成"]
    DraftPR --> End([着手完了（DEVELOPING遷移）])
```

---

## 2. 完了フロー (Wrapup Flow)

`flow-wrapup` Skill 等が担う、品質確保と最終化の詳細な手順です。

```mermaid
flowchart TD
    Complete([実装完了の判断]) --> ReadSkill["💡 開発完了(Developing): 完了処理の開始"]
    ReadSkill --> Validation["最終動作検証（品質チェック）"]
    Validation --> UpdateRoadmap["Roadmapを完了へ"]
    UpdateRoadmap --> CommitPush["Commit & Push"]
    CommitPush --> ReadyPR["Draft PR ➡️ Ready (gh pr ready)"]
    ReadyPR --> Report["完了報告"]
    Report --> End([レビュー待ち（REVIEWING遷移）])
```
