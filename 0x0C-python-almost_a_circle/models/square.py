#!/usr/bin/python3
"""Defines the class Square which is a subclass of Rectangle."""
from rectangle import Rectangle


class Square(Rectangle):
    """Represents Square which inherits Rectangle

    Args:
      size (int): size of the square
      x (int): x coordinate
      y (int): y coordinate
      id (int): identifies the square instance

    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Retruns the print() and str() representation of Square."""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
