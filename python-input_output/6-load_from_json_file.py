#!/usr/bin/python3
"""define function load_from_json_file(filename)"""
import json


def load_from_json_file(filename):
    """creates object from JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
