#!/usr/bin/python3
"""class student that defines a student"""


class Student:
    """define a class student"""

    def __init__(self, first_name, last_name, age):
        """instantiation of class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary representation of student instance"""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attributes of a the student instance"""
        for key, value in json.items():
            setattr(self, key, value)

