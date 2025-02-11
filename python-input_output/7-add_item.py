#!/usr/bin/ptyhon3
"""load, add, save."""


import json
import sys

def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """functon that creates an object from a json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

def add_arguments_to_json():
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, "add_item.json")

if __name__ == "__main__":
    add_arguments_to_json()
