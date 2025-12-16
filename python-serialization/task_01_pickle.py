#!/usr/bin/python3
"""
This module defines a class with/
serialize and deserialize functions
"""
import pickle
class CustomObject:
    """
    This class defines a ccustom object with/
    name, age, is_student
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'w') as f:
                pickle.dump(self, f)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                res = pickle.load(f)
        except:
            return None
        return res
