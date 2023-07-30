#!/usr/bin/python3
""" Defines a class_to_json"""


def class_to_json(obj):
    '''a class returns dictionary description with simple data struct'''
    return obj.__dict__
