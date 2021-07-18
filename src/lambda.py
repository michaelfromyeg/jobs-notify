import json


def lambda_handler(event, context) -> object:
    # TODO implement
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
