#!/usr/bin/python3
"""
This module defines a function that adds attribute
"""


def add_attribute(obj, name, val):
    if type(obj).__module__ != 'builtins':
    # if not isinstance(obj, type) and type(obj).__module__ != 'builtins':
        obj.name = val
    else:
        raise TypeError("can't add new attribute")
