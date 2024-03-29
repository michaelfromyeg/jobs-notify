#!/bin/sh

# Create a lambda function
# Run: sh create-lambda.sh

# Re-used variables
# TODO: set as command line options
FUNCTION_NAME=lambda
REGION=us-east-1
STAGE=test

# Create dependencies export
pip install --target ../package -r ../requirements.txt

# Zip dependencies
cd ../package; zip -r ../build/lambda.zip .; cd ../utils

# Add lambda.py and data.py to dependencies
cd ../src; zip -g ../build/lambda.zip lambda.py data.py notify.py email.html; cd ../utils

# Add dotenv
cd ..; zip -g ./build/lambda.zip .env; cd ./utils

# Create lambda
aws lambda create-function \
    --endpoint-url=http://localhost:4566 \
    --region ${REGION} \
    --function-name ${FUNCTION_NAME} \
    --runtime python3.8 \
    --handler lambda.lambda_handler \
    --memory-size 128 \
    --zip-file fileb:///home/mdema/code/jobs-notify/build/lambda.zip \
    --role arn:aws:iam::000000000000:role/lambda-ex

# TODO: integrate into above call instead of copying dotenv
# aws lambda update-function-configuration
#    --endpoint-url=http://localhost:4566 \
#    --function-name my-function \
#    --environment "Variables={BUCKET=my-bucket,KEY=file.txt}"

# Clean up export
rm -rf ../package
