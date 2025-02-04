#!usr/bin/python3

""" Create a new class name BaseFeometry"""


class BaseGeometry:

    def area(self):
        if not isinstance(self, int):
            raise Exception("aera() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

        def __init__(self, width, height):

            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height
