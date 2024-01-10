#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sep = ['.', '?', ':']
    new_text = ""
    start = 0

    for i, char in enumerate(text):
        if char in sep:
            new_text += text[start:i + 1] + "\n\n"
            start = i + 1
        elif i == len(text) - 1:
            new_text += text[start:]

    print("\n".join(line.strip() for line in new_text.split("\n")))
