#!/usr/bin/python3

def remove_char_at(str, n):
    # Check if n is a valid index
    if n < 0 or n >= len(str):
        return str

    # Create a copy of the string with the character at position n removed
    return str[:n] + str[n + 1:]

# Test cases
if __name__ == "__main__":
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))

