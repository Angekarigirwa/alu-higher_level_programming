#!/usr/bin/python3
"""define class Student"""


class Student:
    """define student instance attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """retrieves dictionary representation"""
        json = dict(vars(self))
        if type(attributes) == list:
            for j in list(json):
                if j not in attributes:
                    json.pop(j, None)
        return json

        return vars(self)
