#!/usr/bin/python3
"""Defines MagicClass class."""

import math


class MagicClass:

    """Represents a magic class."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass instance.

        Args:
            radius (int or float, optional): radius of magic class.
            Defaults to 0.
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Getter method to retrieve the radius of the magic class."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Setter method to set the radius of the magic class.

        Args:
            value (int or float): The new value for the radius.

        Raises:
            TypeError: If the value is not a number (int or float).
        """
        if type(value) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """Calculates the area of the magic class.

        Returns:
            float: The area of the magic class.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the magic class.

        Returns:
            float: The circumference of the magic class.
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":

    magic_obj = MagicClass(5)
    print(magic_obj.area())
    print(magic_obj.circumference())
