#!/usr/bin/python3
"""
Module 3-write_file
"""


def write_file(filename="", text=""):
    """writes to text file and returns characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
