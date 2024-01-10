#!/usr/bin/python3

class MyInt(int):
    """A class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the behavior of the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of the != operator."""
        return super().__eq__(other)

# Example usage:
if __name__ == "__main__":
    # Create instances of MyInt
    a = MyInt(5)
    b = MyInt(10)

    # Inverted behavior for ==
    print(a == b)  # True

    # Inverted behavior for !=
    print(a != b)  # False
