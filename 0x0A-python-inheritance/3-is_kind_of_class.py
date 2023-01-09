#!/usr/bin/python3
"""Defiens a function that checks if a object is instance of a class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
      obj (any): the object to check
      a_class (type): the class to compare to
    Returns:
      True if obj is instance of a_class, otherwise false
    """

    if isinstance(obj, a_class):
        return True
    return False
