#!/usr/bin/python3
"""
This module creates a function that reads a file
"""


def read_file(filename=""):
    """
    This function reads file and print its content
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
