#!/usr/bin/python3
"""defines save_to_json_file after importing json"""
import json


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object to a text file'''
    with open(filename, "w") as fi:
        json.dump(my_obj, fi)
