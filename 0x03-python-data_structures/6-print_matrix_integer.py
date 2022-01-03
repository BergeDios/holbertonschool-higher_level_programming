#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix) - 1
    if not matrix:
        print()
    for row in matrix:
        count = 0
        for i in row:
            if count != 0:
                print(' ', end='')
            print("{:d}".format(i), end='')
            count += 1
        print()
