#!usr/bin/python3

""" Create a new class name BaseFeometry"""


class BaseGeometry:

    def area(self):
        if not isinstance(self, int):
            raise Exception("aera() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
