import argparse
import re
import os

def main():
    parser = argparse.ArgumentParser(description='Update roadmap task status')
    parser.add_argument('--task', required=True, help='Task number (e.g., 4-1)')
    parser.add_argument('--status', required=True, help='New status (e.g., "[/]", "[x]", "[ ]")')
    parser.add_argument('--issue', help='Issue number (e.g., "#61")')
    parser.add_argument('--file', help='Path to roadmap.md (default: docs/status/roadmap.md)')
    
    args = parser.parse_args()
    task_num = args.task
    new_status = args.status
    issue_num = args.issue
    
    # パスの解決
    roadmap_path = args.file if args.file else os.path.join(os.getcwd(), 'docs', 'status', 'roadmap.md')
    if not os.path.exists(roadmap_path):

        print(f"Error: {roadmap_path} not found.")
        return

    with open(roadmap_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    updated = False
    new_lines = []
    
    # 正規表現: タスク番号を含む行を探す
    # 例: - [ ] 4-1. または - [/] #38 2-5.
    # キャプチャグループを使用して、ステータスより前の部分、ステータス、後ろの部分を分ける
    for line in lines:
        # パターン: (^\s*-\s*)(\[.*?\])(\s*)(?:(#\d+)\s+)?(4-1)(\.)
        # 簡易的に: タスク番号 (例: 4-1.) を含む行を探す
        target_pattern = r'(?P<prefix>-\s*)(\[.*?\])(?P<space>\s*)(?P<issue>#\d+\s+)?' + re.escape(task_num) + r'\.'
        
        match = re.search(target_pattern, line)
        if match:
            # ステータスを置換
            line = re.sub(r'\[.*?\]', new_status, line, count=1)
            
            # Issue番号の付与/更新
            if issue_num:
                # すでに Issue があるか確認
                if not match.group('issue'):
                    # ない場合はタスク番号の前に差し込む
                    term = re.escape(task_num) + r'\.'
                    line = re.sub(term, f'{issue_num} {task_num}.', line)
                else:
                    # すでにある場合は上書き（今回は未実装・必要なら）
                    pass
            updated = True
        new_lines.append(line)

    if not updated:
        print(f"Warning: Task {task_num} not found in roadmap.")
    else:
        with open(roadmap_path, 'w', encoding='utf-8', newline='') as f:
            f.writelines(new_lines)
        print(f"Successfully updated task {task_num} in roadmap.")

if __name__ == '__main__':
    main()
