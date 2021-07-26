#!/bin/sh

# Deploy lambda
# ASSUME: `aws configure` has been properly run

FUNCTION_NAME=jobs-notify
REGION=us-west-2

### START Create export

# Create dependencies export
pip install --target ../package -r ../requirements.txt

# Zip dependencies
cd ../package; zip -r ../build/lambda.zip .; cd ../utils

# Add lambda.py and data.py to dependencies
cd ../src; zip -g ../build/lambda.zip lambda.py data.py notify.py email.html; cd ../utils

# Add dotenv
cd ..; zip -g ./build/lambda.zip .env; cd ./utils

### DONE Create export

aws lambda create-function \
    --profile mdema \
    --function-name ${FUNCTION_NAME} \
    --region ${REGION} \
    --zip-file fileb:///home/mdema/code/jobs-notify/build/lambda.zip \
    --handler lambda.lambda_handler \
    --runtime python3.8 \
    --memory-size 128 \
    --role arn:aws:iam::027149006736:role/lambda-ex

# aws lambda invoke --function-name jobs-notify out --log-type Tail