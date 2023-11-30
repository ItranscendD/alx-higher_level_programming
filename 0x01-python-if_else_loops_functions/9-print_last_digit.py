#!/usr/bin/python3

def print_last_digit(number):
    # Get the last digit using the modulo operator
    last_digit = abs(number) % 10

    # Print the last digit without a newline
    print("{}".format(last_digit), end='')

    # Return the value of the last digit
    return last_digit

# Test cases
if _ _name_ _ == "_ _main_ _":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
