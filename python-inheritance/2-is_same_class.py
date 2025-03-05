#!/usr/bin/python3
"""function that returns True if the object is exactly an instance of the
specified class otherswise false"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of
    the specified class"""
    return type(obj) is a_class
