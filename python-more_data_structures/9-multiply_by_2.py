#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = dict(a_dictionary)
    for key, value in newdict.items():
        newdict[key] = value * 2
    return newdict
