#!/usr/bin/python3
import json

"""
Module 7-save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """Writes python obj to file usin json"""

    with open(filename, mode="w", encoding="utf-8"):
        json.dump(my_obj, f)
