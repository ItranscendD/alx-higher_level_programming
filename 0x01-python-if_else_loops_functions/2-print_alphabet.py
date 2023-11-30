#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    print("".join("{}".format(chr(i)) for i in range(ord('a'), ord('z') + 1)))

# Print a newline at the end
print()
