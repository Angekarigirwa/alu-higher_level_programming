#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print(0)
    else:
        sum = 0
        for i in argv[1:]:
            sum += int(i)

        print(sum)
