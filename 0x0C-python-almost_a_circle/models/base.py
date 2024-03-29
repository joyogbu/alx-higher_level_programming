#!/usr/bin/python3
"""creating Base class module"""


import json


class Base:
    """defining the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiating the class with id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON stringrepresentation of
        a list_objs to a file"""
        file_name = cls.__name__ + '.' + 'json'
        _list = []
        with open(file_name, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for i in list_objs:
                    _list.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation
        """
        x = []
        if json_string is None or json_string == []:
            return(x)
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        file_name = cls.__name__ + ".json"
        _list = []
        if file_name is None:
            return ("[]")
        else:
            with open(file_name, encoding="utf-8") as f:
                x = cls.from_json_string(f.read())
                for i in x:
                    _list.append(cls.create(**i))
                    return (_list)
