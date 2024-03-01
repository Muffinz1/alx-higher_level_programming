#!/bin/bash
# methods displayed with a certain url
curl -s -I -X OPTIONS "$i" | grep -i 'Allow' | awk '{print $2}'
