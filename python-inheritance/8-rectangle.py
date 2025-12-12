#!/usr/bin/python3
"""
This module creates a function to check instance
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    This class creates a rectangle with its width and height.
    it inherits from base geometry class.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
