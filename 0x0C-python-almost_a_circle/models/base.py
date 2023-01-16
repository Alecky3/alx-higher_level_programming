#!/usr/bin/python3
"""Contains Base class definition."""


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
