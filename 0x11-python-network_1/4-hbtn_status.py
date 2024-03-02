#!/usr/bin/python3
"""
a python script that will be used to fetch the following link:
https://alx-intranet.hbtn.io/status
using the package requests
"""
import requests


def main():
    """
    fetching the link https://alx-intranet.hbtn.io/status
    for status
    using requests package
    """

    link = 'https://alx-intranet.hbtn.io/status'
    data = requests.get(link)
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))


if __name__ == "__main__":
    main()
