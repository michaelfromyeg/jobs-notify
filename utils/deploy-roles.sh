#!/bin/sh

# Deploy roles for lambda

aws iam create-role \
    --profile mdema \
    --role-name lambda-ex \
    --assume-role-policy-document file://trust-policy.json

aws iam attach-role-policy \
    --profile mdema \
    --role-name lambda-ex \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
