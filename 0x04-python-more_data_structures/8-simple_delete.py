#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

# usage:


if __name__ == "__main__":
    my_dict = {'language': "C", 'number': 89, 'track': "Low level"}

    # Update existing key
    update_dictionary(my_dict, 'language', 'Python')
    print(my_dict)

    # Add a new key
    update_dictionary(my_dict, 'city', 'San Francisco')
    print(my_dict)
