#!/bin/sh

# Delete existing lambda function

aws lambda delete-function \
    --endpoint-url=http://localhost:4566 \
    --function-name lambda