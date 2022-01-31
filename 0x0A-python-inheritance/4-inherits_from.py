#!/usr/bin/python3
"""
Module 4-inherits_from
"""


def inherits_from(obj, a_class):
    """returns t or f if obj is instance of class inherited from specified"""

    if type(obj) is a_class:
       return False

    return issubclass(type(obj), a_class)
