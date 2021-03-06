#!/usr/bin/python3
"""Class Base"""
import json


class Base():
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initilizes attributes for Base Class
        Args:
            id: public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string
        Args:
            list_dictionaries: is a list of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            list_objs: a list of instances who inherit Base
        """

        fn = cls.__name__
        filename = fn + '.json'
        new_list = []

        with open(filename, mode='w', encoding='utf-8') as file_open:
            if list_objs is None:
                file_open.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                file_open.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        import os

        ins_list = []
        fn = cls.__name__
        filename = fn + ".json"
        exists = os.path.isfile(filename)

        if not exists:
            return ins_list

        with open(filename, mode='r', encoding='utf-8') as file_open:
            for line in file_open:
                obj = cls.from_json_string(line)
                for i in obj:
                    ins_list.append(cls.create(**i))

        return ins_list

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            list_objs: a list of instances who inherit Base
        """

        if json_string is None or len(json_string) == 0:
            return ("[]")

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary: can be thought of as a double pointer to a dictionary
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return (dummy)
