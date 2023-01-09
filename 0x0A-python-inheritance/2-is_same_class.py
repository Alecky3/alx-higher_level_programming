#!/usr/bin/python3
"""Defines that compares objects"""


def is_same_class(obj, a_class):
    """Checks id a abj is a exact instance of a class

    Args:
       obj (any): the object to check
       a_class (type): the class to match obj to
    Returns:
      True if obj is a exact instance of a_class,
      false otherwise
    """
    if type(obj) === a_class:
        return True
    return False
