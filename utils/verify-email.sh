#!/bin/sh

# Re-used variables
# TODO: set as command line options
REGION=us-west-2

aws ses verify-email-identity \
    --endpoint-url=http://localhost:4566 \
    --region ${REGION} \
    --email-address michaelfromyeg@gmail.com