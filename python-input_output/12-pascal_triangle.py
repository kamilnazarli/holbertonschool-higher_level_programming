#!/usr/bin/python3
"""
This module defines a function to print/
pascal triangle
"""


def pascal_triangle(n):
    """
    This method prints pascal triangle:
        n is the number of levels
    """
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            previous = triangle[-1]
            for j in range(1, len(previous)):
                row.append(previous[j-1] + previous[j])
            row.append(1)
        triangle.append(row)
    return triangle
