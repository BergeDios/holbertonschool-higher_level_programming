#!/usr/bin/python3
"""

Module 2-rectangle

Class that defines a triangle with pvt att: width and height
Public Methods: area and perimeter

"""


class Rectangle:
    """Class defining a Rectangle
        Attributes: (pvt)Width, (pvt)Height
        Methods: (pub)area, (pub)perimeter"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width value

        Returns:
            private attr width of the rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """Setter methoid for width value

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height value

        Returns:
            private attr height of the rectangle

        """

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height value

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that calculates tha Rectangle area

        Returns:
            rectangle area

        """

        return self.width * self.height
    
    def perimeter(self):
        """Method that calculates the Perimeter

        Returns:
            Rectangles perimeter

        """
        
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
