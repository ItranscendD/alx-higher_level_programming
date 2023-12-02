#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    # Test cases
    index_1 = 2
    index_2 = 10
    index_3 = -1
    new_element = 99

    print(replace_in_list(my_list, index_1, new_element))  # Output: [1, 2, 99, 4, 5]
    print(replace_in_list(my_list, index_2, new_element))  # Output: [1, 2, 3, 4, 5]
    print(replace_in_list(my_list, index_3, new_element))  # Output: [1, 2, 3, 4, 5]
