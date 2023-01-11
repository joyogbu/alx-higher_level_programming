#!/usr/bin/python3
"""class student"""


class Student:
    """representing the student class"""
    def __init__(self, first_name, last_name, age):
        """initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """retrieves a dictionary representation of
        a student instance"""
        return self.__dict__
