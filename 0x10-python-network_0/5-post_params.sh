#!/bin/bash
# Bash script that takes in a URL , POST request to the passed URL, displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
