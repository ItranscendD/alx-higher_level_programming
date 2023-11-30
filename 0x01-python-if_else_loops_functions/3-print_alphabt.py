#!/usr/bin/python3

# Use a single print function with string format to print the alphabet, excluding 'q' and 'e'
print("".join("{}".format(chr(i)) for i in range(ord('a'), ord('z') + 1) if chr(i) not in ('q', 'e')), end='')
