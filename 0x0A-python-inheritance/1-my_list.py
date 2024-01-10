#!/usr/bin/python3

class MyList(list):
    """A class that inherits from list and provides additional methods."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage:
if __name__ == "__main__":
    # Create an instance of MyList
    my_list_instance = MyList([4, 2, 8, 1, 5])

    # Call the print_sorted method to print the sorted list
    my_list_instance.print_sorted()
