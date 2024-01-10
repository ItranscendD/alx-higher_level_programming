#!/usr/bin/python3

class BaseGeometry:
    """A class representing base geometry operations."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value for being an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Example usage:
if __name__ == "__main__":
    # Create an instance of BaseGeometry
    geometry = BaseGeometry()

    # Example of calling area method (raises an exception)
    try:
        geometry.area()
    except Exception as e:
        print(f"Exception: {e}")

    # Example of calling integer_validator method
    try:
        geometry.integer_validator("side_length", 5)
        geometry.integer_validator("side_length", -2)  # This should raise a ValueError
        geometry.integer_validator("side_length", "not_an_integer")  # This should raise a TypeError
    except Exception as e:
        print(f"Exception: {e}")
