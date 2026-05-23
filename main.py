import requests
import os
from dotenv import load_dotenv
load_dotenv()
from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()   # reads env vars automatically


from graph import app


def fetch_pr_files(owner, repo, pr_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    files = []

    for f in data:
        files.append({
            "file_name": f["filename"],
            "diff": f.get("patch", ""),
            "full_file": ""  # optional: fetch separately if needed
        })

    return files



def run_pr(owner, repo, pr_number):

    files = fetch_pr_files(owner, repo, pr_number)

    result = app.invoke({
        "files": files,
    },config={"callbacks": [langfuse_handler]}
    )

    return result["aggregated"]