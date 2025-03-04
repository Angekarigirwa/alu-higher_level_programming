#!/usr/bin/python3
"""a square class"""


class Square:
    """
    a square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize size and position variable"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ size."""
        return self.__size

    @size.setter
    def size(self, size):
        """size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __init__(self, size=0, position=(0, 0)):
        """assign"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, val):
        """assign a size to a value"""
        self.__size = val
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ position."""
        return self.__position

    @position.setter
    def position(self, val):
        """Sets position to a value."""
        self.__position = val
        if not isinstance(val, tuple) or len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(val[0], int) or not isinstance(val[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns area of square"""
        sarea = self.__size * self.__size
        return sarea

    def my_print(self):
        """prints square whith  # sign"""
        if self.__size == 0:
            print()
        else:
            for v in range(self.__position[1]):
                print()
            for s in range(self.__size):
                for j in range(self.__position[0]):
                    print(' ', end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
