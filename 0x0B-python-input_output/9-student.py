#!/usr/bin/python3
"""
Module 11-student

"""


class Student():
    """student class  """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary description with simple data structure """
        return self.__dict__
