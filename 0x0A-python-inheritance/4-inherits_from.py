#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

# Example usage:
if __name__ == "__main__":
    # Test the function with different objects and classes
    class BaseClass:
        pass

    class SubClass(BaseClass):
        pass

    instance_of_base = BaseClass()
    instance_of_sub = SubClass()
    instance_of_int = 42

    print(inherits_from(instance_of_base, BaseClass))  # True
    print(inherits_from(instance_of_sub, BaseClass))  # True

    # False cases
    print(inherits_from(instance_of_int, BaseClass))  # False
    print(inherits_from(instance_of_int, int))  # False
