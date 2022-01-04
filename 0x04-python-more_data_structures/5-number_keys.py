#!/usr/bin/python3


def number_keys(a_dictionary):
    numofkeys = 0
    list_keys = list(a_dictionary.keys())
    for keys in list_keys:
        numofkeys += 1
    return (numofkeys)
