#!/usr/bin/python3
""" read file function"""


def read_file(filename=""):
    """reads a file and prints it out"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
