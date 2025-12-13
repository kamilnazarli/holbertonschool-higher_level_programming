#!/usr/bin/python3
"""
This module creates a func that returns/
dict for JSON serialization
"""


def class_to_json(obj):
    """
    This function returns the dict version
    """
    return obj.__dict__
