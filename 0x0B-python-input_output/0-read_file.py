#!/usr/bin/python3

''' Defining a function that reads a text file (UTF8) then prints'''


def read_file(filename=""):
    ''' Scripting The Function That Reads The txt File Then prints '''
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
