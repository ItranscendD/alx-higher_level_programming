#!/usr/bin/python3
"""
Class Student that defines a student.
"""

class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: A dictionary containing the specified attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary representing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/10-student.txt")
