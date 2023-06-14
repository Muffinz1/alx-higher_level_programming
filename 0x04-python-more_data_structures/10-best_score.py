#!/usr/bin/python3
def best_score(my_dict):
    if my_dict == {} or my_dict is None:
        return None
    maximum = max(my_dict.values())
    for value, key in my_dict.items():
        if value is maximum:
            return key
