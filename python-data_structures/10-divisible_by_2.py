#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d = []
    for j in my_list:
        if j % 2 == 0:
            d.append(True)
        else:
            d.append(False)
    return d
