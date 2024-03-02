#!/usr/bin/python3
"""
 a Python script that takes in a URL and an email
 sends a POST request to the passed URL
 email as a parameter
 displays the body of the response (decoded in utf-8)
"""

from sys import argv as a
import urllib.request


def main():
    """
    In the main function to get the email:
    The email must be sent in the email variable
    using the packages urllib and sys
    with the email as a parameter
    displays the body of the response
    """

    link = a[1]
    mail = {'email': a[2]}
    mail_data = urllib.parse.urlencode(mail)
    coded_mail_data = mail_data.encode('utf8')
    new_link = urllib.request.Request(link, coded_mail_data)

    with urllib.request.urlopen(new_link) as data:
        readable_data = data.read()
        print(readable_data.decode('utf-8'))


if __name__ == "__main__":
    main()
