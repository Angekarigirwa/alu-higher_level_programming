#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = 0
    for key, value in a_dictionary.items():
        keys += 1
    return int(keys)
