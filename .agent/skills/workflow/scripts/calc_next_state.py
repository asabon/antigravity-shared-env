import argparse
import json
import sys

def get_next_state(current_status, current_phase, action, issue_num="-", pr_num="-"):
    # デフォルトの維持
    next_status = current_status
    next_phase = current_phase
    next_issue = issue_num
    next_pr = pr_num

    # 1. 強制グローバルアクション
    if action == '/dev-pause':
        return 'IDLE', '-', "-", "-"
    
    if action == '/cleanup':
        return 'ACTIVE', 'PLANNING', "-", "-"

    # 2. IDLE 時の遷移
    if current_status == 'IDLE':
        if action == '/dev-start':
            return 'ACTIVE', 'PLANNING', next_issue, next_pr
        else:
            # IDLE 時は他のアクションによる遷移を基本認めない（ロック）
            return 'IDLE', '-', "-", "-"

    # 3. ACTIVE 時のフェーズ遷移
    if current_status == 'ACTIVE':
        if action == 'issue-create':
            next_phase = 'PREPARING'
        elif action == 'kickoff':
            next_phase = 'DEVELOPING'
        elif action == 'ready':
            next_phase = 'REVIEWING'
        elif action == 'review-comment':
            # 既存PRでの修正
            next_phase = 'DEVELOPING'
        elif action == '/dev-start':
            # 継続中での re-start
            pass 

    return next_status, next_phase, next_issue, next_pr

def main():
    parser = argparse.ArgumentParser(description='Calculate next workflow state.')
    parser.add_argument('--status', required=True, choices=['ACTIVE', 'IDLE'], help='Current status')
    parser.add_argument('--phase', required=True, choices=['PLANNING', 'PREPARING', 'DEVELOPING', 'REVIEWING', '-'], help='Current phase')
    parser.add_argument('--action', required=True, help='Action executed (e.g., /cleanup, /dev-pause, ready, kickoff)')
    parser.add_argument('--issue', default='-', help='Issue number (e.g., #65)')
    parser.add_argument('--pr', default='-', help='PR number (e.g., #66)')

    args = parser.parse_args()

    next_status, next_phase, next_issue, next_pr = get_next_state(
        args.status, args.phase, args.action, args.issue, args.pr
    )

    # ステータスバー文字列の組み立て
    status_bar = ""
    if next_status == 'ACTIVE':
        status_bar = f"【📊 状態: ACTIVE | フェーズ: {next_phase} | Issue: {next_issue} | PR: {next_pr}】"
    else:
        # IDLE時はIssue/PRも表示しない
        status_bar = f"【📊 状態: IDLE | フェーズ: -】"

    result = {
        "current": {
            "status": args.status,
            "phase": args.phase,
            "action": args.action
        },
        "next": {
            "status": next_status,
            "phase": next_phase,
            "issue": next_issue,
            "pr": next_pr
        },
        "status_bar": status_bar
    }

    # 標準出力に結果を表示
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
