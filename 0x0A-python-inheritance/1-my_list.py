#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """ class inherited from list """

    def print_sorted(self):
        """ prints a list sorted """

        sorted_list = self.copy()
        sorted_list = sorted(sorted_list)
        print(sorted_list)
