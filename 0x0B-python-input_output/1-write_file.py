#!/usr/bin/python3
"""Defines a function that writes text to file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of
    characters written
    """

    count = 0
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)

    return (count)
