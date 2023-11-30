#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase letter to uppercase using ASCII values
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end='')
        else:
            # Print non-lowercase characters as is
            print("{}".format(char), end='')

    # Print a newline at the end
    print()

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")

