#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)

# Example usage:
if __name__ == "__main__":
    # You can test the function with different objects
    # For example, let's create a simple class and an instance
    class ExampleClass:
        def __init__(self):
            self.attribute1 = "value1"

        def method1(self):
            print("This is method1")

    example_instance = ExampleClass()

    # Call the lookup function on the instance
    result = lookup(example_instance)
    print(result)
