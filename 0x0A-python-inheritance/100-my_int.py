#!/usr/bin/python3
"""
Module 100-my_int.py
"""


class MyInt(int):
    """myint has operator inverted == !="""

    def __eq__(a, b):
        return (a is b)

    def __ne__(a, b):
        return (a is not b)
