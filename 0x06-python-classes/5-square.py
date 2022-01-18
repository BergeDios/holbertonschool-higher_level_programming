#!/usr/bin/python3
"""
Module 5-square
Class Square, Private Size, Public Area
Able to print square based on size with # and get and set size
"""


class Square:
    """Class Square defines object

    Attribute:
        size (int): size of square
        area (int): size of square ** 2

    Functions:
        __init__
        area(self)
        size(self)
        size(self, value)
        my_print(self)
    """

    def __init__(self, size=0):
        """Initialization method of object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """method returns size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method returns area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """method to print a '#' size square"""
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
