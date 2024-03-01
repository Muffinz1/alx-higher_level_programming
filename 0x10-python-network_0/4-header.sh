#!/bin/bash
# a Bash script that takes in a URL as an argument and gets the url then display the body of response
curl -s "$1" -H "X-School-User-Id: 98"
