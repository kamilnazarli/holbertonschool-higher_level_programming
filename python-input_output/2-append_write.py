#!/usr/bin/python3
"""
This module defines a function that adds text to the end of a file
"""


def append_write(filename="", text=""):
    """
    This function adds the text to te end of a file
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        written = f.write(text)
    return written
