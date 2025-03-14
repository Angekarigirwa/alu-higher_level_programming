#!/usr/bin/python3
"""define function save_to_json_file(my_obj, filename)"""
import json


def save_to_json_file(my_obj, filename):
    """Save Object to a JSON file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
