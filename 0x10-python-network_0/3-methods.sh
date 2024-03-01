#!/bin/bash
# methods displayed with a certain url
curl -s -X OPTIONS "$i" -i | grep -i "Allow:" | cut -f2- -d" "
