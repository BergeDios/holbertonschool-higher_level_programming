#!/usr/bin/python3
"""

Module 9-rectangle

Class that defines a triangle with pvt att: width and height
Public Methods: area and perimeter, str update, repr update


"""


class Rectangle:
    """Class defining a Rectangle
        Attributes: (pvt)Width, (pvt)Height
        Methods: (pub)area, (pub)perimeter"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Method that returns rectangle filled with #

        Returns:
            rectangle as str of #

        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle
        for line in range(self.height):
            rectangle += ((str(self.print_symbol) * self.width) + "\n")
        return rectangle[:-1]

    def __repr__(self):
        """Methodreturns the string representation of the isntance for eval

        Returns:
            string representation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method to do somethifn when instance deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns bigger or equal rectangle

        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2

        Raises:
            TypeError: when some arg is not of rectangle class

        Returns:
            the bigger rect or 1 if equal

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method returns new rectangle object but with width = heigth = size

        Args:
            cls: rectangle class
            size: rectangle width and rectangle height

        Returns:
            a new instance of Rectangle class

        """

        return cls(size, size)
