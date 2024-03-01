#!/bin/bash
# methods displayed with a certain url
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
