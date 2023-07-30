#!/usr/bin/python3
""" Defines a class_to_json"""


def class_to_json(obj):
    '''a class that returns the dictionary description with simple data structure'''
    return obj.__dict__
