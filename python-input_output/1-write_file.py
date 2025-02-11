#!/usr/bin/python3
"""write files"""


def write_file(filename="", text=""):
    """function that write a string to a text file (UTF8)"""
    with open(filename, encoding="utf-8") as file:
        return file.write(text)
