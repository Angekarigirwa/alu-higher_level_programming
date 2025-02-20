#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value1 = list(a_dictionary.items())[0][1]
    key1 = list(a_dictionary.items())[0][0]

    for key, value in a_dictionary.items():
        if value > value1:
            value1 = value
            key1 = key
    return key1
