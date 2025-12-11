#!/usr/bin/python3
"""
This module creates a class MyList which derives from list
"""


class MyList(list):
    """
    This class inherits from list class,
    and add one method.
    """
    def print_sorted(self):
        self.sort()
