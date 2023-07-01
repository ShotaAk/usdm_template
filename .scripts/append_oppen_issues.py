#!/usr/bin/env python3

import re
import argparse
<<<<<<< HEAD
import sys
from get_open_issues_from_github import get_open_issues

# args = sys.argv

# # .adocファイルのパス
# adoc_file_path = args[1]

# print(adoc_file_path)

# # GitHubのリポジトリ情報
# repository_owner = "ShotaAk"
# repository_name = "usdm_template"

# # .adocファイルの内容を読み込む
# with open(adoc_file_path, "r") as file:
#     adoc_content = file.read()

# # 正規表現を使用して、:id:行で始まる行を検索
# pattern = r"^:id:\s*(\S+)"
# matches = re.findall(pattern, adoc_content, re.MULTILINE)

# # 各IDに対してGitHubのIssueを検索し、URLを取得して.adocファイルに追記
# for issue_id in matches:
#     issue_url = f"https://github.com/{repository_owner}/{repository_name}/issues/{issue_id}"
#     adoc_content = re.sub(f":id:\s*{issue_id}", f":id: {issue_id}\n:issue: {issue_url}", adoc_content, count=1)

# # 書き換えた.adocファイルを保存
# with open(adoc_file_path, "w") as file:
#     file.write(adoc_content)
=======
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
>>>>>>> origin/main

def main():
    parser = argparse.ArgumentParser(description='Append GitHub issue URLs to .adoc files')
    parser.add_argument('adoc_file', type=str, help='AsciiDoc file path')
    parser.add_argument('owner', type=str, help='GitHub repository owner')
    parser.add_argument('repository', type=str, help='GitHub repository name')

    args = parser.parse_args()
<<<<<<< HEAD

=======
>>>>>>> origin/main
    adoc_file_path = args.adoc_file
    owner = args.owner
    repository = args.repository

    # .adocファイルの内容を読み込む
    with open(adoc_file_path, "r") as file:
        adoc_content = file.read()

<<<<<<< HEAD
    # 正規表現を使用して、:id:行で始まる行を検索し、仕様IDのリストを取得
    pattern = r"^:id:\s*(\S+)"
    spec_ids = re.findall(pattern, adoc_content, re.MULTILINE)

    # GitHubからオープンなIssueを取得
    open_issues = get_open_issues(owner, repository)

    # 各IDに対してGitHubのIssueを検索し、URLを取得して.adocファイルに追記
    for spec_id in spec_ids:
        matching_issues = []
        for issue in open_issues:
            spec_id_of_issue = issue["title"].split(" ")[0]
            if spec_id == spec_id_of_issue:
                matching_issues.append(issue)

        # 追記する文字列を生成
        text = ""
        for issue in matching_issues:
            text += "{}[Issue #{},title={}], ".format(issue["html_url"], issue["number"], issue["title"])
        
        # .adocファイルに追記
        if text != "":
            adoc_content = re.sub(f":id:\s*{spec_id}", f":id: {spec_id}\n:open_issues: {text}", adoc_content, count=1)
=======
    # .adocファイルから仕様IDを抽出
    spec_id_list = get_spec_id_list(adoc_content)

    # GitHubリポジトリからオープンなIssueを抽出
    open_issues = get_open_issues(owner, repository)

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
>>>>>>> origin/main

    # 書き換えた.adocファイルを保存
    with open(adoc_file_path, "w") as file:
        file.write(adoc_content)

if __name__ == '__main__':
    main()
