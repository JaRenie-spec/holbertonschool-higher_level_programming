#!/usr/bin/python3

"""function takes an object as an argument
and returns a list of its attributes and methods."""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
