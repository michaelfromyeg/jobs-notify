#!/bin/sh

# Clean-up the build folder by deleting all zip files

find . -name "../build/*.zip" -type f -delete
find . -name "../build/*.json" -type f -delete
