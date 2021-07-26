import requests
from typing import List, Tuple

# The list of repositories to target
repos = (
    "pittcsc/Summer2022-Internships",
    "quantprep/quantinternships2022",
    "ChrisDryden/Canadian-Tech-Internships-Summer-2022",
)


def fetch_jobs(time: str) -> Tuple[List[str], List[str]]:
    """
    Send email with the latest internship postings.
    """
    # The number of new commits
    count = 0

    # The string content for the email
    html_list: List[str] = []
    plaintext_list: List[str] = []

    for repo in repos:
        api_url = f"https://api.github.com/repos/{repo}/commits?since={time}"

        # The JSON response of recent commites (since `time`)
        commits = requests.get(
            api_url, headers={"Accept": "application/vnd.github.v3+json"}
        ).json()
        for commit in commits:
            commit_message: str = commit["commit"]["message"]
            commit_url: str = commit["html_url"]
            commit_author: str = commit["commit"]["author"]["name"]
            commit_date: str = commit["commit"]["author"]["date"]

            plaintext_message = create_plaintext_item(
                repo, commit_message, commit_url, commit_author, commit_date
            )
            html_message = create_html_item(
                repo, commit_message, commit_url, commit_author, commit_date
            )

            plaintext_list.append(plaintext_message)
            html_list.append(html_message)

            count += 1

    print(f"There were {count} commits made!")

    return [plaintext_list, html_list]


def create_html_item(
    repo, commit_message, commit_url, commit_author, commit_date
) -> str:
    """Return a formatted HTML entry"""
    return f'<li>{repo}: <a href="{commit_url}">{commit_message}</a> by {commit_author} on {commit_date}</li>'


def create_plaintext_item(
    repo, commit_message, commit_url, commit_author, commit_date
) -> str:
    """Return a formatted plaintext entry."""
    return (
        f"{repo}: {commit_message} <{commit_url}> by {commit_author} on {commit_date}"
    )
