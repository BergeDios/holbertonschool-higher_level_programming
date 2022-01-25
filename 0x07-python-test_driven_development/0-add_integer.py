#!/usr/bin/python3
"""

Module 0-add_integer
adds two numbers

"""


def add_integer(a, b=98):
    """Funtion that adds two ints and/or float nums

    Args:
        a: first number
        b: second number

    Returns:
        The addition of a and b

    Raises:
        TypeError: if a or b aren't integer and/or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
