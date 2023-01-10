#!/usr/bin/python3
"""Defines a function that save JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file, using JSON Representation."""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
