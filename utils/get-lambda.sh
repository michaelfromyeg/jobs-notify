#!/bin/sh

# List all active lambda functions

aws --endpoint-url=http://localhost:4566 lambda list-functions
