#!/bin/sh

# Create role for lambda

aws iam create-role \
    --endpoint-url=http://localhost:4566 \
    --role-name lambda-ex \
    --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

aws iam attach-role-policy \
    --endpoint-url=http://localhost:4566 \
    --role-name lambda-ex \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
