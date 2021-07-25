#!/bin/sh

# Get AWS identity

aws sts get-caller-identity \
    --endpoint-url=http://localhost:4566