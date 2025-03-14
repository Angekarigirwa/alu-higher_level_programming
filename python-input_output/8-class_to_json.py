#!/usr/bin/python3
"""define function class_to_json(obj)"""


def class_to_json(obj):
    """return dictionary description for json serialization of an object"""
    return vars(obj)
