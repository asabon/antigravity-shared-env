# シーケンス図 (Sequence Diagrams)

アクター（ユーザー・AIエージェント・GitHub）間のメッセージや、各状態（フェーズ）でのキャッチボールを定義します。

---

## 1. PLANNING 状態（計画・タスク選定）

```mermaid
sequenceDiagram
    participant U as ユーザー
    participant A as Antigravity
    participant L as ローカル環境 (FS/Git)
    participant G as GitHub (Cloud)

    Note over U, G: 💡 [計画・タスク選定の開始] (新規 / cleanup後 等)

    A->>L: roadmap.md の読込 (高速)
    A->>U: 追加・修正案の提示
    U->>A: 承認・修正依頼
    A->>L: roadmap.md の更新 (高速)
    A->>U: 次の作業の提案
    U->>A: 着手対象を **選択**
    
    alt Issueあり
        A->>G: Issue を読む (API通信)
    else Issueなし
        A->>G: Issue 起票 (API通信)
    end
```

---

## 2. PREPARING 状態（準備）

※ブランチ作成に関して、一貫性担保のため **GitHub 上で先にブランチを発行** しローカルへ引き込む「GitHub-First」を採用します。

```mermaid
sequenceDiagram
    participant U as ユーザー
    participant A as Antigravity
    participant L as ローカル環境 (Git/FS)
    participant G as GitHub (Cloud)

    Note over U, G: 💡 [準備・着手 (Preparing) の開始]

    A->>G: 開発ブランチの作成（Issueとの紐付け）
    G-->>A: （ブランチ名等の返却）
    A->>L: 開発ブランチのチェックアウト
    A->>L: task.md の初期化（Issueからの詳細書き出し）
    A->>G: 空コミットの Push ＆ Draft PR の作成
    A->>U: 準備完了・開発（DEVELOPING）開始の報告
```

---

## 3. DEVELOPING 状態（実装ループ）

```mermaid
sequenceDiagram
    participant U as ユーザー
    participant A as Antigravity
    participant L as ローカル環境 (Git/FS)
    participant G as GitHub (Cloud)

    Note over U, G: 💡 [開発 (Developing) の開始]

    rect rgb(240, 240, 240)
        Note over A, L: 🔁 開発ループ (Iterative Loop)
        A->>L: コード修正 / 実装
        A->>L: テスト / 動作確認
        A->>L: task.md の更新 (進捗管理)
    end

    Note over A, L: 💡 [開発完了フェーズ]
    A->>L: 最終動作検証 (品質チェック)
    A->>L: roadmap.md の更新 (着手中 ➡️ 完了)
    
    A->>G: 最終 Commit & Push
    A->>G: Draft PR ➡️ Ready for Review (`gh pr ready`)
    
    A->>U: 開発完了・レビュー依頼の報告
```

---

## 4. REVIEWING 状態（レビュー・後処理）

```mermaid
sequenceDiagram
    participant U as ユーザー
    participant A as Antigravity
    participant L as ローカル環境 (Git/FS)
    participant G as GitHub (Cloud)

    Note over U, G: 💡 [レビュー待機 (Reviewing) の開始]

    U->>G: PR のレビュー実施 (コメント or 承認)

    alt 指摘あり（要修正）
        U->>A: チャットで直接「修正依頼（機能・要件など）」を指示
        A->>U: 修正対応を開始します（DEVELOPING 遷移）
    else 承認 ＆ マージ完了
        U->>G: PR 承認 ＆ マージ実行
        U->>A: `/cleanup`（クリーンアップを依頼）
        A->>L: ローカルブランチの削除（クリーンアップ）
        A->>U: 全ての作業が完了しました（PLANNING 遷移）
    end
```
