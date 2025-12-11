#!/usr/bin/python3
"""
This module creates a function to check instance
"""


def is_same_class(obj, a_class):
    """
    This method checks an object whether
    it is an instance of a specific class
    """
    return type(obj) is a_class
