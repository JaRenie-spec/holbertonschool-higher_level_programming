#!/usr/bin/python3
"""initialize and empty dictionary to be serialized"""


import json

data = {}


def serialize_and_save_to_file(data, filename):
    """serialize and save data to the specified file"""
    with open(filename, "w") as file:
        json.dump(data, file)


serialize_and_save_to_file(data, 'data.json')


def load_and_deserialize(filename):
    """load and deserialize data from the specified file"""
    with open(filename, "r") as file:
        data_un = json.load(file)
        print(data_un)


load_and_deserialize('data.json')
