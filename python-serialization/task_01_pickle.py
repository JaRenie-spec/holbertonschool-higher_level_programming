#!/usr/bin/python3
"""Class representing a custom object"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """initializes a new CustomObject instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displays the attribute of the object"""
        if not isinstance(self.name, str):
            raise TypeError
        print("Name:", self.name)
        if not isinstance(self.age, int):
            raise TypeError
        print("Age:", self.age)
        if not isinstance(self.is_student, bool):
            raise ValueError
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """serializes the object"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserializes the object"""
        with open(filename, "rb") as file:
            cls = pickle.load(file)
        return cls
