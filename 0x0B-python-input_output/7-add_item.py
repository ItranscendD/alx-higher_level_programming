#!/usr/bin/python3
"""
Script to add arguments to a Python list and save them to a file.
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_and_save():
    """Adds all arguments to a Python list and saves them to a file."""
    # Check if the file exists
    filename = "add_item.json"

    # Load existing list or create a new one
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_and_save()
