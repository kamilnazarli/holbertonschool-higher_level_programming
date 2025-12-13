#!/usr/bin/python3
"""
This module defines Student class
"""


class Student:
    """
    This class defines a student/
    by their first, last name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            temp = {}
            for i in attrs:
                if self.__dict__.get(i) is not None:
                    temp.update({i: self.__dict__.get(i)})
            return temp
