#!/usr/bin/ptyhon3
"""save object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
