#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    num_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in num_dict.keys():
            return 0
        elif num_dict[i] >= num_dict[j]:
            num += num_dict[i]
        else:
            num -= num_dict[i]
    num += num_dict[roman_string[-1]]
    return num
