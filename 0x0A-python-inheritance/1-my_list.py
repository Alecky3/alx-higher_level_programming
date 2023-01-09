#!/usr/bin/python3
"""Defines a class that inherits list."""


class MyList(list):
    """Inherits list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
