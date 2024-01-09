#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: Instance of a class.

    Returns:
        Dictionary description of the object.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-class_to_json.txt")
