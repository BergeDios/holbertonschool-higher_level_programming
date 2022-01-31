#!/usr/bin/python3
"""
Module 101-add_attribute
"""


def add_attribute(obj, name, value):
    """ adds new a new attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
        
    setattr(obj, name, value)
