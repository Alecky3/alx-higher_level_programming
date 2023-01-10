#!/usr/bin/python3
"""Defines a function that returns the __dict__ for JSON
Serializable object
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """

    return obj.__dict__
