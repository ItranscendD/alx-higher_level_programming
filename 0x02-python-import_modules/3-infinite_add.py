#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    sum_result = 0

    if argc > 1:
        for i in range(1, argc):
            sum_result += int(argv[i])

    print("{}".format(sum_result))
