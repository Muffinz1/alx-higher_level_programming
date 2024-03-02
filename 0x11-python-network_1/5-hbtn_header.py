#!/usr/bin/python3
"""
 a Python script that takes in a URL
 sends a request to the URL using the requests liberary
 displays the value of the X-Request-Id variable
 found in the header of the response
"""

from sys import argv as a
import requests


def main():
    """
    the main function takes in a link then sends a request to that link
    it demands a response and after fetching the data
    it prints the variable found in the header of that response
    """
    link = a[1]
    data = requests.get(link)
    print(data.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
