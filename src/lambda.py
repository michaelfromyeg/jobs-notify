import os
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv, find_dotenv
from notify import generate_email

DEBUG = True


def lambda_handler(event, context) -> object:
    """Push event into SQS."""
    load_dotenv(find_dotenv())

    [subject, plaintext_email, html_email] = generate_email()

    response = send_email(
        subject=subject, plaintext_email=plaintext_email, html_email=html_email
    )

    return {
        "statusCode": 200,
        "body": {"message": "ok", "response": response},
    }


def send_email(subject: str, plaintext_email: str, html_email: str) -> None:
    """
    Send email via SES.
    """
    recipient = os.environ["TO_EMAIL"]
    sender = os.environ["FROM_EMAIL"]

    configuration_set = "ConfigSet"
    aws_region = os.environ["AWS_REGION"]
    charset = "utf-8"

    # TODO: create lambda with correct permissions
    client = boto3.client(
        "ses",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=aws_region,
    )

    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [
                    recipient,
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": charset,
                        "Data": html_email,
                    },
                    "Text": {
                        "Charset": charset,
                        "Data": plaintext_email,
                    },
                },
                "Subject": {"Charset": charset, "Data": subject},
            },
            Source=sender,
            ConfigurationSetName=configuration_set,
        )

        print(f"Email sent! Message ID: {response['MessageId']}")

        return response
    except ClientError as e:
        print(e.response["Error"]["Message"])
