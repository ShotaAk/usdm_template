
import requests

def get_open_issues(repo_owner, repo_name, access_token=""):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

    headers = {}
    if access_token != "":
        headers = {"Authorization": f"Bearer {access_token}"}
    params = {"state": "open"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        issues = response.json()
        return issues
    else:
        print(f"Request failed with status code {response.status_code}")
        return None