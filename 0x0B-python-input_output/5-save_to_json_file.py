#!/usr/bin/python3
"""
Module with load_from_json_file function.
"""

import json

def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file containing the JSON representation.

    Returns:
        The Python object created from the JSON representation.

    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    load_from_json_file()
