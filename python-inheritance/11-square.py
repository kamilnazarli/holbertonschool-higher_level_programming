#!/usr/bin/python3
"""
This module defines Square class inherited from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    To define a square with its size
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        return self.__size * self.__size
