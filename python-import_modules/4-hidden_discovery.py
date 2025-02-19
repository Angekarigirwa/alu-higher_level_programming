#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    values = dir(hidden_4)
    values.sort()
    for i in values:
        if i[:2] != "__":
            print(i)
