#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char

    print("{}".format(result))

# Test cases
if __name__ == "__main__":
    uppercase("Holberton")
    uppercase("Holberton School")
    uppercase("Holberton School, 98 battery street")
