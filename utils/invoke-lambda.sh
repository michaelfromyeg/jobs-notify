#!/bin/sh

# List lambda function

aws lambda invoke \
    --endpoint-url=http://localhost:4566 \
    --function-name lambda \
    "../build/response.json"