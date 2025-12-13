#!/usr/bin/python3
"""
This module creates a function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes JSON representation to a file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
