#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_string = my_string[:]
    x = 0
    for i in range(length):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new_string[:(i - x)] + new_string[(i + 1 - x):]
            x += 1
    return (new_string)
