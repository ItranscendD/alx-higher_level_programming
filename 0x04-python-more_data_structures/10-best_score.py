#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key

# Example usage:


if __name__ == "__main__":
    my_dict = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

    # Find the student with the best score
    best_student = best_score(my_dict)
    print("Best student:", best_student)
