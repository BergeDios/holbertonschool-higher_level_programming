#!/usr/bin/python3
"""
Module 6-square
"""


class Square:
    """Class defines square by size, area and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Method of initialization of square object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """method to return size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ method returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ method to set position value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """method returnin square size **2"""
        return (self.__size ** 2)

    def my_print(self):
        """method prints a # square according to size value"""

        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for p in range(self.size):
                    print("#", end="")
                print()
