#!/usr/bin/python3
"""class square"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """ private instance attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")

    def area(self):
        sarea = self.__size * self.__size
        return sarea
