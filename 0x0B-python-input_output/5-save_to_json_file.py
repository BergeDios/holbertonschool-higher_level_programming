#!/usr/bin/python3
"""
Module 7-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes python obj to file usin json"""

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
