import json
import argparse
import sys

def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="MarkdownをGitHub MCP用の完璧なJSONペイロードに変換します")
    parser.add_argument("input_file", help="読み込むMarkdownファイルのパス (例: draft.md)")
    parser.add_argument("--repo", required=True, help="リポジトリ名 (例: tinyalg/notion-mcp-challenge)")
    parser.add_argument("--path", required=True, help="GitHub上の保存先パス (例: posts/notion-mcp-challenge.md)")
    parser.add_argument("--branch", required=True, help="ブランチ名 (例: submission-update-1)")
    parser.add_argument("--message", default="Update submission post from Notion", help="コミットメッセージ")
    parser.add_argument("--sha", help="更新時の既存ファイルのSHA (新規作成時は不要)")

    args = parser.parse_args()

    try:
        # Markdownファイルを読み込む
        with open(args.input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"エラー: ファイル '{args.input_file}' が見つかりません。")
        sys.exit(1)

    # MCPツールに渡すための引数（arguments）オブジェクトを構築
    payload = {
        "repo": args.repo,
        "path": args.path,
        "branch": args.branch,
        "message": args.message,
        "content": markdown_content
    }

    # SHAが指定されている場合は追加
    if args.sha:
        payload["sha"] = args.sha

    # json.dumps が「改行(\n)」「ダブルクォート(\")」「バッククォート」など
    # すべての厄介な文字を【完璧に】エスケープしてくれます！
    escaped_json = json.dumps(payload, indent=2, ensure_ascii=False)

    # 結果を output_payload.json に書き出す
    output_filename = "output_payload.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(escaped_json)

    print(f"✅ 成功: 完璧にエスケープされたJSONを '{output_filename}' に出力しました。")
    print("このファイルの中身をClaudeに渡すか、直接APIに投げてください！")

if __name__ == "__main__":
    main()