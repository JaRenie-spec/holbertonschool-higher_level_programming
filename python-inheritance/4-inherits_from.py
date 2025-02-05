#!usr/bin/python3

"""define a function that checks if an object is a subclass inherited
from a specified class."""


def inherits_from(obj, a_class):
    """Return true if obj is an instance of a class"""
    return issubclass(int, a_class)
