#!/usr/bin/python3
"""
This module defines a function which shows all available attributes
"""


def lookup(cls):
    """
    This function returns all attributes inside a class
    """
    return dir(cls)
