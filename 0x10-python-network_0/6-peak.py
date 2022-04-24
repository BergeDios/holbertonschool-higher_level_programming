#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that is greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    else:
        l = list_of_integers
        l.sort()
        return (l[-1])
