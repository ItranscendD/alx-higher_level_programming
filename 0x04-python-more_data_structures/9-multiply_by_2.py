#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict

# usage:


if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Multiply all values by 2
    new_dict = multiply_by_2(my_dict)
    print(new_dict)
