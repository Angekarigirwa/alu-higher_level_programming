#!/usr/bin/python3
"""function that returns True if the object
is an instance of a class that inherited
 (directly or indirectly) from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """checks if the object is an instance of
    a class that inherited from the specified class"""
    return isinstance(obj, a_class) and type(obj) !=  a_class
