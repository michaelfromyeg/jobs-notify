#!/bin/sh

# Verify email address

aws ses verify-email-identity \
    --profile mdema \
    --email-address michaelfromyeg@gmail.com