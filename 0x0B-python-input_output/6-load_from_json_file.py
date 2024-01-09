#!/usr/bin/python3
"""
Module with save_to_json_file function.
"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object to be serialized and written to the file.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

if __name__ == "__main__":
    save_to_json_file()
