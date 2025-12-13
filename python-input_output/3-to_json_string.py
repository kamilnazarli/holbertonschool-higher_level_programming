#!/usr/bin/python3
"""
This module creates a function that returns json represantation of an object
"""
import json


def to_json_string(my_obj):
    """
    This function returns JSON represantation
    """
    return json.dumps(my_obj)
