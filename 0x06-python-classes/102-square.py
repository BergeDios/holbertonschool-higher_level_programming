#!/usr/bin/python3
"""
Module 4-square
Class Square, Private Size, Public Area
Can access and update size
"""


class Square:
    """Defines Square object

    Args:
        size (int): size of square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """initialization method of square

        Attributes:
            size (int): default 0 or size, not private due to usage of setter
        """
        self.size = size

    @property
    def size(self):
        """Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter

        Args:
            value: sets size to value, with exceptions
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of square
        """
        return (self.__size ** 2)

    def __lt__(self, other):
        """< comparison function override"""
        return((self.area()) < (other.area()))

    def __le__(self, other):
        """<= comparison function override"""
        return((self.area()) <= (other.area()))
    
    def __eq__(self, other):
        """== comparison function override"""
        return((self.area()) == (other.area()))
    
    def __ne__(self, other):
        """!= comparison function override"""
        return((self.area()) != (other.area()))
    
    def __gt__(self, other):
        """> comparison function override"""
        return((self.area()) > (other.area()))
    
    def __ge__(self, other):
        """>= comparison function override"""
        return((self.area()) >= (other.area()))
