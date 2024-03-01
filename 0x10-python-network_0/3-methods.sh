#!/bin/bash
# methods displayed with a certain url
curl -s -X OPTIONS "$i" -i | grep -i "Allow:" | awk '{print $2}'
