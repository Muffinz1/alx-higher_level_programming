#!/usr/bin/python3
"""Defines a load_from_json file”"""
import json


def load_from_json_file(filename):
    '''a function that creates an Object from a JSON file'''
    with open(filename) as fi:
        return json.load(fi)

