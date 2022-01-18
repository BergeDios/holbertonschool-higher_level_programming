#!/usr/bin/python3
"""
Module 1-square
Defines a Class Square object with prvt attr size
"""
class Square:
    """Class with object with private attribute size"""
    def __init__(self, size):
        """Initialization method storing size as well

        Args:
            param1: size of the square
        """
        self.__size = size
