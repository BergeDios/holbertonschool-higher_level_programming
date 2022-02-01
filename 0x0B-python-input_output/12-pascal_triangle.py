#!/usr/bin/python3
"""
Module 14-pascal_triangle
"""


def pascal_triangle(n):
    """returns matrix with pascal triangle"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        line = [1]
        for i in range(rows):
            line.append(triangle[-1][i] + triangle[-1][i+1])
        line.append(1)
        triangle.append(l)
        return triangle
