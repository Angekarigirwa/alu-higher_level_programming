#!/usr/bin/python3
"""function append_write"""


def append_write(filename="", text=""):
    """append a string  at the end of text file and returns characters added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
