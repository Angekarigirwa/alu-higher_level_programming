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
        json_l = dict(vars(self))
        if type(attributes) == list:
            for j in list(json_l):
                if j not in attributes:
                    json.pop(j, None)
        return json_l

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for i in list(json):
            setattr(self, i, json[i])
