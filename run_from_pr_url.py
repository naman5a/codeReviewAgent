import os
import re
import requests
from dotenv import load_dotenv

from graph import app

load_dotenv()


# -----------------------------
# 1. Parse PR URL
# -----------------------------
def parse_pr_url(url: str):
    """
    Example:
    https://github.com/expressjs/express/pull/7275/changes
    """

    match = re.search(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)", url)

    if not match:
        raise ValueError("Invalid GitHub PR URL")

    owner = match.group(1)
    repo = match.group(2)
    pr_number = match.group(3)

    return owner, repo, pr_number


# -----------------------------
# 2. Fetch PR files from GitHub API
# -----------------------------
def fetch_pr_files(owner, repo, pr_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(f"GitHub API error: {res.text}")

    data = res.json()

    files = []

    for f in data:
        files.append({
            "file_name": f["filename"],
            "diff": f.get("patch", ""),
            "full_file": ""  # optional upgrade later
        })

    return files


# -----------------------------
# 3. Run full PR review pipeline
# -----------------------------
def run_pr_from_url(pr_url: str):
    owner, repo, pr_number = parse_pr_url(pr_url)

    files = fetch_pr_files(owner, repo, pr_number)

    result = app.invoke({
        "files": files
    })

    return result["aggregated"]


# -----------------------------
# 4. CLI entry
# -----------------------------
if __name__ == "__main__":

    url = "https://github.com/expressjs/express/pull/7275/changes"

    output = run_pr_from_url(url)

    print("\n===== FINAL PR REVIEW =====\n")
    print(output)