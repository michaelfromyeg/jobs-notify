#!/bin/sh

# Update a lambda function

FUNCTION_NAME=lambda

zip -j '../build/lambda.zip' '../src/lambda.py' '../src/data.py'

aws lambda create-function \
    --endpoint-url=http://localhost:4566 \
    --function-name ${FUNCTION_NAME} \
    --zip-file "fileb:///home/mdema/code/jobs-notify/build/lambda.zip"