#!/usr/bin/python3
"""
This module creates a function that writes a specific text to the file
"""


def write_file(filename="", text=""):
    """
    This function writes a specific text to the file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

