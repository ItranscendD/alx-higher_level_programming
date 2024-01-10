#!/usr/bin/python3
"""Module containing the Square class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        super().__init__(size, size)

    def __str__(self):
        """Return the square description.

        Returns:
            str: The square description in the format [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.width, self.height)

# Example usage:
if __name__ == "__main__":
    # Create a Square instance
    try:
        my_square = Square(4)
        print(my_square)
        print("Area:", my_square.area())
    except Exception as e:
        print(e)
