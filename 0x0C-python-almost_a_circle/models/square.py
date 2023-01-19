#!/usr/bin/python3
"""Defines the class Square which is a subclass of Rectangle."""
from models.rectangle import Rectangle


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

    @property
    def size(self):
        """Gets/Sets the size of the square."""
        return self.width

    @size.setter
    def size(self, width):
        self.width = width
        self.height = width

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        Args:
          *args (list): the argumets to use for updating the attributes
          **kwargs (dict): the arguments to use for updating the attribues
                           when *args are not present
        """
        count = 0
        if args and len(args) != 0:
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
