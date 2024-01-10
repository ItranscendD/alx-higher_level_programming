#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class; otherwise, False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class; otherwise, False.
    """
    return isinstance(obj, a_class)

# Example usage:
if __name__ == "__main__":
    # Test the function with different objects and classes
    instance_of_str = "Hello"
    instance_of_int = 42
    instance_of_list = [1, 2, 3]

    print(is_kind_of_class(instance_of_str, str))  # True
    print(is_kind_of_class(instance_of_int, int))  # True
    print(is_kind_of_class(instance_of_list, list))  # True

    # False cases
    print(is_kind_of_class(instance_of_str, int))  # False
    print(is_kind_of_class(instance_of_int, list))  # False
    print(is_kind_of_class(instance_of_list, str))  # False
