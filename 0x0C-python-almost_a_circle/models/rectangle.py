#!/usr/bin/python3
"""Defines 'Rectangle' class."""
from base import Base


class Reactangle(Base):
    """ Represents 'Rectangle' class which is a subclass of 'Base'."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a new 'Rectangle'

        Args:
          width (int): width of the rectangle
          height (int): height of the rectangle
          x (int): the x coordinate of the rectangle
          y (int): y coordinate of the rectangle
          id (int): identifies the reactangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle."""
        self.__width = width

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle."""
        self.__height = height

    @property
    def x(self):
        """Returns the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x coordinate."""
        self.__x = x

    @property
    def y(self):
        """Returns the y coordinate."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y coordinate."""
        self.__y = y
