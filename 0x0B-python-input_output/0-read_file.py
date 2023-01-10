#!/usr/bin/python3
"""Defines reading a text file function."""


def read_file(filename=""):
    """Reads the contsnts of a text file and prints
    to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
