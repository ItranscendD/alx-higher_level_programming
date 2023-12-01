#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    
    # Test cases
    index_1 = 2
    index_2 = 10
    index_3 = -1
    
    print(element_at(my_list, index_1))  # Output: 3
    print(element_at(my_list, index_2))  # Output: None
    print(element_at(my_list, index_3))  # Output: None
