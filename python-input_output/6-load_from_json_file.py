#!/usr/bin/python3
"""
This module creates a function that creates an object from/
a JSON file
"""
import json


def load_from_json_file(filename):
    """
    This function loads an object from a file
    """
    with open(filename, encoding="utf-8") as f:
        res = json.load(my_obj, f)
    return res
