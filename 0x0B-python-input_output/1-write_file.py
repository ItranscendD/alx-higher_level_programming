#!/usr/bin/python3

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)

if __name__ == "__main__":
    write_file()
