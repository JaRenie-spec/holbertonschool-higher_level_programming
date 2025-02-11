#!/usr/bin/python3
"""create object from a Json file"""


import json

def load_from_json_file(filename):
    """function that creates an object from a json file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
