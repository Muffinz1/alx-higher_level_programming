#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None  or my_dict == {}:
        return None
    maximum = max(my_dict.values())
    for value, key in my_dict.items():
        if value is maximum:
            return key
