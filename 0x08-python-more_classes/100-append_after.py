#!/usr/bin/python3
"""
Function append_after(filename="", search_string="", new_string="") that
inserts a line of text to a file after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after each line containing the search string.
    """
    lines = []

    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/13-append_after.txt")
