import requests
from dotenv import load_dotenv
from typing import List, Tuple

# The list of repositories to target
repos = (
    "pittcsc/Summer2022-Internships",
    "quantprep/quantinternships2022",
    "ChrisDryden/Canadian-Tech-Internships-Summer-2022",
)

DEBUG = True


def fetch_jobs(time: str) -> Tuple[List[str], List[str]]:
    """
    Send email with the latest internship postings.
    """

    # Load environment variables from project root
    load_dotenv()

    count = 0
    html_list = []
    plaintext_list = []
    for repo in repos:
        for res in requests.get(
            f"https://api.github.com/repos/{repo}/commits?since={time}",
            headers={"Accept": "application/vnd.github.v3+json"},
        ).json():
            if DEBUG:
                print(f"Updated commit {res}")
            plaintext_list.append(
                f"{repo}: {res['commit']['message']} <{res['html_url']}> by {res['commit']['author']['name']} on {res['commit']['author']['date']}"
            )
            html_list.append(
                f"<li>{repo}: <a href=\"{res['html_url']}\">{res['commit']['message']}</a> by {res['commit']['author']['name']} on {res['commit']['author']['date']}</li>"
            )
            count += 1

    print(f"There were {count} commits made!")

    return [plaintext_list, html_list]
