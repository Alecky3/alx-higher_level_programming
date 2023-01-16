#!/usr/bin/python3
"""Defines 'Rectangle' class."""
from base import Base


class Rectangle(Base):
    """ Represents 'Rectangle' class which is a subclass of 'Base'."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a new 'Rectangle'

        Args:
          width (int): width of the rectangle
          height (int): height of the rectangle
          x (int): the x coordinate of the rectangle
          y (int): y coordinate of the rectangle
          id (int): identifies the reactangle
        Raises:
          TypeError: if either of width, height, x or y is not an integer
          ValueError: if either of width or height <= 0
          ValueError: if either x or y is < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets/Sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets/Sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets/Sets the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Sets/Gets the y coordinate."""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle."""

        return (self.width * self.height)

    def display(self):
        """Prints in stdout the Rectangle instance
        with the character #.
        """
        for r in range(self.height):
            for y in range(self.width):
                print("#", end="")

            print()

    def __str__(self):
        """Returns the str() and print() representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )
