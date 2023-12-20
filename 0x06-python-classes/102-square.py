#!/usr/bin/python3
"""Defines Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int or float, optional): size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int or float): The new value for the size.

        Raises:
            TypeError: If the value is not a number (int or float).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison for squares based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison for squares based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison for squares based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison for squares based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison for squares based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison for squares based on area."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
