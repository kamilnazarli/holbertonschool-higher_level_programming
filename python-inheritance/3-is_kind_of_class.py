#!/usr/bin/python3
"""
This module creates a function to check instance
"""


def inherits_from(obj, a_class):
    """
    This method checks an object whether
    it is an instance of a specific class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
