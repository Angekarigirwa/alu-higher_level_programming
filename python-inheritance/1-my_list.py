#!/usr/bin/python3
"""define class mylist"""


class MyList(list):
    """ class MyList that inherits from list"""

    def print_sorted(self):
        """returns list in sorted order"""
        s_list = self[:]
        s_list.sort()
        print("{}".format(s_list))
