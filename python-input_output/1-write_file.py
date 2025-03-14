#!/usr/bin/python3
"""function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns number of characters"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
