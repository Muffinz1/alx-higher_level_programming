#!/usr/bin/python3
"""defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    ''' a function that returns True if the object is an instance of
    or if the object is instance of a class that inherited '''
    if isinstance(obj, a_class):
        return True
    return False
