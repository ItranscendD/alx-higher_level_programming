#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if "__dict__" in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

# Example usage:
if __name__ == "__main__":
    # Create a simple class
    class ExampleClass:
        pass

    # Create an instance of the class
    obj_instance = ExampleClass()

    # Add a new attribute to the instance
    add_attribute(obj_instance, "new_attribute", "new_value")

    # Print the added attribute
    print(obj_instance.new_attribute)
