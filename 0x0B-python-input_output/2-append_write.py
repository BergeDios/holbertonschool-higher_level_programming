#!/usr/bin/python3
"""
Module 4-append_write
"""


def append_write(filename="", text=""):
    """append to text and retunr char added"""

    with open(filename, mode="a", encoding="utf=8") as f:
        return(f.write(text))
