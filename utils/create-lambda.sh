#!/bin/sh

# Create (or update) a lambda function

FUNCTION_NAME=lambda
REGION=us-east-1
STAGE=test

zip -j '../build/lambda.zip' '../src/lambda.py'

aws lambda create-function \
    --endpoint-url=http://localhost:4566 \
    --region ${REGION} \
    --function-name ${FUNCTION_NAME} \
    --runtime python3.8 \
    --handler lambda.lambda_handler \
    --memory-size 128 \
    --zip-file "fileb:///home/mdema/code/jobs-notify/build/lambda.zip" \
    --role arn:aws:iam::123456:role/irrelevant