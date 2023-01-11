#!/usr/bin/python3
"""class student"""


class Student:
    """representing the student class"""
    def __init__(self, first_name, last_name, age):
        """initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a student instance"""
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            return {i: v for i, v in self.__dict__.items() if i in attrs}
        return self.__dict__
