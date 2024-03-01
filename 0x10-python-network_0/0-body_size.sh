#!/bin/bash
# A Bash script that takes in a URL
curl -sI "$1" | grep -i "content-length" | awk '{print $2}'
