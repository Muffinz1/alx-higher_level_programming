#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    flip = my_list[::-1]
    for i in range(len(flip)):
        print("{:d}".format(flip[i]))
