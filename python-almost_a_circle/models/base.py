#!/usr/bin/python3
"""define class base"""

import json
import csv


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instance attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of list dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        dictionary_list = None
        if list_objs is not None:
            dictionary_list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dictionary_list))

    def from_json_string(json_string):
        """list of json string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class instance"""
        if cls.__name__ == 'Rectangle':
            size = cls(4, 2)
        else:
            size = cls(2)
        size.update(**dictionary)
        return size

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        try:
            with open(cls.__name__ + '.json') as f:
                txt = f.read()
                return [cls.create(**i) for i in cls.from_json_string(txt)]
        except FileNotFoundError:
            return []
