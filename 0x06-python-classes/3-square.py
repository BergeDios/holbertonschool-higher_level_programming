#!/usr/bin/python3
"""
Module 3-square
"""


class Square:
    """Class square defines object by size and public area"""
    def __init__(self, size=0):
        """method of initialization of square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method returning square area of object"""
        return (self.__size ** 2)
