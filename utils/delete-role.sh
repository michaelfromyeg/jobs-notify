#!/bin/sh

# Delete role for lambda

aws iam delete-role-policy \
    --endpoint-url=http://localhost:4566 \
    --role-name lambda-ex \
    --policy-name AWSLambdaBasicExecutionRole

aws iam delete-role \
    --endpoint-url=http://localhost:4566 \
    --role-name lambda-ex
