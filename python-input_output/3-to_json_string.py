#!/usr/bin/python3
import json
"""
This module creates a function that returns json represantation of an object
"""


def to_json_string(my_obj):
    """
    This function returns JSON represantation
    """
    return json.dumps(my_obj)
