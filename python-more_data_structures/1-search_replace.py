#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list.copy()
    if not my_list:
        return list
    for item in range(len(my_list)):
        if list[item] == search:
            list[item] = replace
    return list
