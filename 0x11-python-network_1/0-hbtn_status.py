#!/usr/bin/python3
"""
a python script that will be used to fetch the following link:
https://alx-intranet.hbtn.io/status
using the package urllib
"""
import urllib.request


def main():
    """
    a main function that is used to fetch a link given to it
    decode it in a certain format
    """

    link = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(link) as data:
        readable_data = data.read()
        print("Body response: ")
        print("\t- type: {}".format(type(readable_data)))
        print("\t- content: {}".format(readable_data))
        print("\t- utf8 content: {}".format(readable_data.decode('utf8')))


if __name__ == "__main__":
    main()
