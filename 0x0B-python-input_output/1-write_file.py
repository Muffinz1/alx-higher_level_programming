#!/usr/bin/python3
'''Defines a function that writes a file'''


def write_file(filename="", text=""):
    '''scriptting the function to cast a UTF8 text file.'''
    with open(filename, "w", encoding="utf-8") as fi:
        return fi.write(text)
