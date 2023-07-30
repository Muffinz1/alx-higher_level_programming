#!/usr/bin/python3
"""defines a function called to_json_string"""
import json


def to_json_string(my_obj):
    ''' a function that returns a json dumb'''
    return json.dumps(my_obj)
