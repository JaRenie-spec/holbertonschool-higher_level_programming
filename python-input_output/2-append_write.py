#!/usr/bin/python3
"""append files"""


def append_write(filename="", text=""):
    """function that appends a string"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
