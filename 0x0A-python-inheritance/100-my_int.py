#!/usr/bin/python3
"""Defines  MyInt class subclass of int."""


class MyInt(int):
    """Represents Invert subclass which is a rebel"""

    def __eq__(self, value):
        """Overrides super().__eq__()"""
        return self.real != value

    def __ne__(self, value):
        """Overrides super().__ne__()"""
        return self.real == value
