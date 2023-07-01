
import requests

def get_open_issues(github_repo, access_token=""):
    url = f"https://api.github.com/repos/{github_repo}/issues"

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