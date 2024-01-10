i#!/usr/bin/python3
"""Module containing the Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

# Example usage:
if __name__ == "__main__":
    # Create an instance of Rectangle
    rectangle_instance = Rectangle(10, 5)

    # Accessing width and height attributes
    print(rectangle_instance.__width)  # This will raise an AttributeError
