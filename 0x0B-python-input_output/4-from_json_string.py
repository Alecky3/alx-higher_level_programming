#!/usr/bin/python3
"""Defines a function that converts JSON string to object."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""

    return json.loads(my_str)
