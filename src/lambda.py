import json
from datetime import datetime, timedelta
from data import fetch_jobs


def lambda_handler(event, context) -> object:
    """Push event into SQS."""

    # Get the current time; check the previous day
    time = (datetime.now() - timedelta(days=1)).isoformat()

    [plaintext_list, html_list] = fetch_jobs(time)

    return {
        "statusCode": 200,
        "body": {
            "plaintext": "\n".join(plaintext_list),
            "html": "\n".join(html_list),
        },
    }
