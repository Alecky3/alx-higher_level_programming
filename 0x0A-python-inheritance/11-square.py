#!/usr/bin/python3
"""Defines Square Class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represnts Square class."""

    def __init__(self, size):
        """Initializes a Rectangle

        Args:
         size (int): the size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
