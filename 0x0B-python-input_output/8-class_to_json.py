#!/usr/bin/python3
"""
Module 10-class_to_json
"""


def class_to_json(obj):
    """returns dictionary description for json obj"""

    return obj.__dict__
