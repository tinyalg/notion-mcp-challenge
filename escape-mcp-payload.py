import json
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate perfect JSON payload for GitHub MCP tools")
    parser.add_argument("--tool", choices=["push", "file", "create_pr", "update_pr"], required=True, 
                        help="Target tool: 'push', 'file', 'create_pr', or 'update_pr'")
    
    # 共通の引数
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    
    # 【変更点1】単一の長文テキスト用（PRのbodyや、create_or_update_fileのcontent用）
    parser.add_argument("--text-input", help="Path to the text file (Required for 'file', 'create_pr', 'update_pr')")
    
    # 【変更点2】push_files用の複数ファイル指定
    # 使い方: --file draft.md posts/draft.md --file image.png assets/image.png
    parser.add_argument("--file", nargs=2, action="append", metavar=("LOCAL_PATH", "REMOTE_PATH"), 
                        help="Local path and remote path. Can be specified multiple times. (Required for 'push')")

    # 個別の引数
    parser.add_argument("--branch", help="Branch name (required for 'push', 'file', and 'create_pr')")
    parser.add_argument("--path", help="File path (required for 'file' tool)")
    parser.add_argument("--message", default="Automated update from Notion", help="Commit message")
    parser.add_argument("--sha", help="Existing file SHA (optional, only for 'file')")
    parser.add_argument("--title", help="PR title (required for 'create_pr')")
    parser.add_argument("--pr-number", type=int, help="PR number (required for 'update_pr')")
    parser.add_argument("--base", default="main", help="Base branch (for 'create_pr')")

    args = parser.parse_args()

    payload = {}

    if args.tool == "push":
        if not args.file:
            print("Error: At least one '--file LOCAL REMOTE' is required for 'push' tool.")
            sys.exit(1)
        
        files_payload = []
        for local_path, remote_path in args.file:
            try:
                # 複数ファイルを順番に読み込んで配列に追加していく
                with open(local_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                files_payload.append({
                    "path": remote_path,
                    "content": content
                })
            except FileNotFoundError:
                print(f"Error: File '{local_path}' not found.")
                sys.exit(1)

        payload = {
            "owner": args.owner,
            "repo": args.repo,
            "branch": args.branch,
            "message": args.message,
            "files": files_payload
        }

    else:
        # push以外のツールは、今まで通り1つのテキストファイル（--text-input）を読み込む
        if not args.text_input:
            print(f"Error: --text-input is required for tool '{args.tool}'.")
            sys.exit(1)
            
        try:
            with open(args.text_input, 'r', encoding='utf-8') as f:
                long_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.text_input}' not found.")
            sys.exit(1)

        if args.tool == "file":
            payload = {
                "owner": args.owner,
                "repo": args.repo,
                "branch": args.branch,
                "path": args.path,
                "message": args.message,
                "content": long_text
            }
            if args.sha:
                payload["sha"] = args.sha
        elif args.tool == "create_pr":
            payload = {
                "owner": args.owner,
                "repo": args.repo,
                "head": args.branch,
                "base": args.base,
                "title": args.title,
                "body": long_text
            }
        elif args.tool == "update_pr":
            payload = {
                "owner": args.owner,
                "repo": args.repo,
                "pullNumber": args.pr_number,
                "body": long_text
            }

    # 完璧にエスケープして出力
    output_filename = "payload.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(payload, indent=2, ensure_ascii=False))

    print(f"✅ Success: Payload for '{args.tool}' generated to '{output_filename}'")

if __name__ == "__main__":
    main()