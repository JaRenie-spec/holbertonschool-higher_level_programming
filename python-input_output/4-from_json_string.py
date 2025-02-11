#!/usr/bin/python3
"""from json string to object"""


import json

def from_json_string(my_str):
    """functin that returns an object represented by a json string"""
    return json.loads(my_str)
