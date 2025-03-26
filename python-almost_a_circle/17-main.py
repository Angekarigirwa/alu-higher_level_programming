#!/usr/bin/python3
""" 17-main """
from models.square import Square

if __name__ == "__main__":

    r1 = Square(2)
    r1_dictionary = r1.to_dictionary()
    r2 = Square.create(**{'size': 2})
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
