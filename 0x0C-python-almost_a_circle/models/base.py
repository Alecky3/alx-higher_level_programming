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
