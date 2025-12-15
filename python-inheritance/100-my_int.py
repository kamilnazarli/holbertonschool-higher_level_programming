#!/usr/bin/python3
"""
This module a class MyInt
"""


class MyInt(int):
    """
    This class inverts the functionalities
    """

    def __init__(self, my_int):
        self.my_int = my_int

    def __eq__(self, val):
        return self.my_int != val

    def __ne__(self, val):
        return self.my_int == val
