#!/usr/bin/python3
"""class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """define class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area of the rectangle"""
        A = self.width * self.height
        return A

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for j in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        try:
            if type(args) == tuple and len(args) > 0:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
                return
            try:
                self.id = kwargs['id']
            except Exception:
                pass
            try:
                self.width = kwargs.get('width')
            except Exception:
                pass
            try:
                self.height = kwargs.get('height')
            except Exception:
                pass
            try:
                self.x = kwargs.get('x')
            except Exception:
                pass
            try:
                self.y = kwargs.get('y')
            except Exception:
                pass
        except Exception:
            pass

    def to_dictionary(self):
        """dictionary representation"""
        return{"id": self.id, "width": self.width,
               "height": self.height, "x": self.x, "y": self.y}
