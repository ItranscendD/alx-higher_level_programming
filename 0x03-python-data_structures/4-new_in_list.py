#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

# Example usage:
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5]
    new_index = 2
    new_element = 99
    
    # Test case
    modified_list = new_in_list(original_list, new_index, new_element)
    print("Original List:", original_list)
    print("Modified List:", modified_list)
