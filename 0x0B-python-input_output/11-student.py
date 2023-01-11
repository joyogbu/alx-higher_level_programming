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

    def reload_from_json(self, json):
        """replace all attributes of the Student instance"""
        #d = {}
        for i, v in json.items():
            #d[i] = v
            #d[i] = v
            self.__dict__ = json
        #print("hd is {}".format(d))
            #return(d)
        
