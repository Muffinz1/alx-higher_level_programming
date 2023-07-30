#!/usr/bin/python3
"""Defines a function called append write"""


def append_write(filename="", text=""):
    '''scripting the function to append text to file'''
    with open(filename, 'a', encoding="utf-8") as fi:
        return fi.write(text)
