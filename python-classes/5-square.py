#!/usr/bin/python3
"""class square"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """init size"""
        self.__size = size

    @property
    def size(self):
        "size attribute"
        return self.__size

    @size.setter
    def size(self, size):
        """ assigning"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")

    def area(self):
        sarea = self.__size * self.__size
        return sarea

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for s in range(self.__size):
                for k in range(self.__size):
                    print("#", end="")
                print()
