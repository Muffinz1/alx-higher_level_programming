#!/bin/bash
# A Bash script that takes in a URL
# Sends a GET request to the URL	
# Displays the body of the responsei

curl -sI "$1" | grep -i content-length | cut -d " " -f 2
