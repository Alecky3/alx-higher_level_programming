#!/usr/bin/python3
"""Defines Student class."""


class Student:
    """Represents Student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary of a student instance."""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {elem: getattr(self, elem) for elem in attrs if
                    hasattr(self, elem)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
