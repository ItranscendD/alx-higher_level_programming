#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square with a private size attribute."""
    
    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
