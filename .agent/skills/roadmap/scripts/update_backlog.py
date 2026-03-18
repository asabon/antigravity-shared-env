import argparse
import re
import os

def main():
    parser = argparse.ArgumentParser(description='Move items in backlog.md')
    parser.add_argument('--task', required=True, help='Task description or part of it')
    parser.add_argument('--status', required=True, choices=['Sorted', 'Analyzing', 'Unsorted'], help='Target section')
    parser.add_argument('--file', help='Path to backlog.md (default: docs/status/backlog.md)')
    
    args = parser.parse_args()
    task_text = args.task
    target_section = args.status
    
    backlog_path = args.file if args.file else os.path.join(os.getcwd(), 'docs', 'status', 'backlog.md')
    if not os.path.exists(backlog_path):
        print(f"Error: {backlog_path} not found.")
        return

    with open(backlog_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # セクションごとに分割
    # 想定ヘッダー: ## 未分類 (Unsorted), ## 整理済 (Sorted), ## 検討中 (Analyzing)
    sections = re.split(r'(##\s+.*?\(.*?\))', content)
    
    if len(sections) < 2:
        print("Error: Could not parse backlog structure.")
        return

    new_sections = list(sections)
    moved_item = None

    # 1. 該当アイテムの検索と削除
    for i in range(1, len(new_sections), 2):
        header = new_sections[i]
        body_index = i + 1
        if body_index >= len(new_sections):
            break
        body = new_lines = new_sections[body_index]
        
        # アイテム行を探す (例: - アイテムテキスト)
        lines = body.splitlines()
        filtered_lines = []
        for line in lines:
            if task_text in line and line.strip().startswith('-'):
                moved_item = line
                print(f"Found item: {line}")
            else:
                filtered_lines.append(line)
        new_sections[body_index] = '\n'.join(filtered_lines) + ('\n' if filtered_lines else '')

    if not moved_item:
        print(f"Error: Task '{task_text}' not found in backlog.")
        return

    # 2. 移動先セクションへの追加
    # target_section (例: 'Sorted') を含むヘッダーを探す
    target_header_index = -1
    for i in range(1, len(new_sections), 2):
        if target_section in new_sections[i]:
            target_header_index = i
            break

    if target_header_index == -1:
        print(f"Error: Section '{target_section}' not found in backlog.")
        return

    # 移動先セクションの本文の末尾に追記
    target_body_index = target_header_index + 1
    if target_body_index < len(new_sections):
        body = new_sections[target_body_index]
        if body.endswith('\n'):
            new_sections[target_body_index] = body + moved_item + '\n'
        else:
            new_sections[target_body_index] = body + '\n' + moved_item + '\n'
    else:
        new_sections.append('\n' + moved_item + '\n')

    # ファイル書き込み
    new_content = ''.join(new_sections)
    with open(backlog_path, 'w', encoding='utf-8', newline='') as f:
        f.write(new_content)
        
    print(f"Successfully moved '{task_text}' to '{target_section}'.")

if __name__ == '__main__':
    main()
