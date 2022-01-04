#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    if matrix is not None:  # checks matrix existance
        new_matrix = []
        for rows in matrix:  # for each row append the num to the power of 2
            new_matrix.append(list(map(lambda x: x**2, rows)))
        return (new_matrix)
    return None
