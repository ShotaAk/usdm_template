#!/usr/bin/env python3

import re
import argparse
from get_open_issues_from_github import get_open_issues

def get_spec_id_list(adoc_content):
    # 正規表現を使用して、:id:行で始まる行を検索し、仕様IDのリストを取得
    pattern = r"^:id:\s*(\S+)"
    spec_id_list = re.findall(pattern, adoc_content, re.MULTILINE)

    return spec_id_list

def get_spec_id_matching_github_issues(spec_id, open_issues):
    matching_issues = []
    for issue in open_issues:
        spec_id_of_issue = issue["title"].split(" ")[0]
        if spec_id == spec_id_of_issue:
            matching_issues.append(issue)

    return matching_issues

def main():
    parser = argparse.ArgumentParser(description='Append GitHub issue URLs to .adoc files')
    parser.add_argument('adoc_file', type=str, help='AsciiDoc file path')
    parser.add_argument('github_repo', type=str, help='GitHub repository name. e.g. "owner/repository"')

    args = parser.parse_args()
    adoc_file_path = args.adoc_file
    github_repo = args.github_repo

    # .adocファイルの内容を読み込む
    with open(adoc_file_path, "r") as file:
        adoc_content = file.read()

    # .adocファイルから仕様IDを抽出
    spec_id_list = get_spec_id_list(adoc_content)

    # GitHubリポジトリからオープンなIssueを抽出
    open_issues = get_open_issues(github_repo)

    for spec_id in spec_id_list:
        # 仕様IDが一致知るIssueを抽出
        matching_issues = get_spec_id_matching_github_issues(spec_id, open_issues)

        # 追記する文字列を生成
        appending_text = ""
        for issue in matching_issues:
            appending_text += "{}[Issue #{},title={}], ".format(issue["html_url"], issue["number"], issue["title"])
        
        # .adocファイルに追記
        if appending_text != "":
            adoc_content = re.sub(f":id:\s*{spec_id}", f":id: {spec_id}\n:open_issues: {appending_text}", adoc_content, count=1)

    # 書き換えた.adocファイルを保存
    with open(adoc_file_path, "w") as file:
        file.write(adoc_content)

if __name__ == '__main__':
    main()
