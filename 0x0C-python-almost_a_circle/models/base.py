#!/usr/bin/python3
"""Contains Base class definition."""
import json


class Base:
    """Represents  'Base' class

    Attributes:
       __nb_objects (int): number of instantiated 'Base' instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes 'Base' class
        Args:
          id (int) : id of new Base
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
          list_dictionaries (list): list of dictionaries

        Returns: JSON string
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""

        save_file = cls.__name__ + ".json"

        with open(save_file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
          json_string (str): string representing a list of dictionaries.
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set

        Args:
          **dictionary (dict): dictionary of attributes
        """

        if dictionary and dict != {}:
            if str(cls.__name__) == 'Rectangle':
                obj = cls(10, 10)
            else:
                obj = cls(10)
            obj.update(**dict)

        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_dictionaries]
        except IOError:
            return []
