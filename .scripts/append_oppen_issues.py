#!/usr/bin/env python3

import re
import requests
import sys

args = sys.argv

# .adocファイルのパス
adoc_file_path = args[1]

print(adoc_file_path)

# GitHubのリポジトリ情報
repository_owner = "ShotaAk"
repository_name = "usdm_template"

# .adocファイルの内容を読み込む
with open(adoc_file_path, "r") as file:
    adoc_content = file.read()

# 正規表現を使用して、:id:行で始まる行を検索
pattern = r"^:id:\s*(\S+)"
matches = re.findall(pattern, adoc_content, re.MULTILINE)

# 各IDに対してGitHubのIssueを検索し、URLを取得して.adocファイルに追記
for issue_id in matches:
    issue_url = f"https://github.com/{repository_owner}/{repository_name}/issues/{issue_id}"
    adoc_content = re.sub(f":id:\s*{issue_id}", f":id: {issue_id}\n:issue: {issue_url}", adoc_content, count=1)

# 書き換えた.adocファイルを保存
with open(adoc_file_path, "w") as file:
    file.write(adoc_content)
