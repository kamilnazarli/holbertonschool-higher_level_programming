#!/usr/bin/python3
"""
This module creates a function that returns from json represantation to python
"""
import json


def from_json_string(my_obj):
    """
    This function returns python represantation
    """
    return json.loads(my_obj)
