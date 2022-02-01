#!/usr/bin/python3
"""
Module 8-load_from_json_file

"""
import json


def load_from_json_file(filename):
    """Creates a Python obj from JSON file"""

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
