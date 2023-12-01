#!/usr/bin/python3
def no_c(my_string):
    filtered_string = ""
    for char in my_string:
        if char.lower() != 'c':
            filtered_string += char
    return filtered_string

# Example usage:
if __name__ == "__main__":
    test_strings = ["Best School", "Chicago", "C is fun!"]
    for test_string in test_strings:
        result = no_c(test_string)
        print(result)
