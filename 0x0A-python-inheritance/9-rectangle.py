#!/usr/bin/python3
"""
Module 8-base_geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """emptyclass"""
    
    def area(self):

        return self.__width * self.__height

    def integer_validator(self, name, value):
        """ validates value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        """ ponele """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
