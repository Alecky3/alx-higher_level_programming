#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and returns the number of characters added.
    """

    count = 0
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)

    return (count)
