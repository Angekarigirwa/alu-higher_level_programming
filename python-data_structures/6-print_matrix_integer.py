#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for value in matrix:
        if not value:
            print()
        else:
            for i in value:
                if i == value[-1]:
                    print('{:d}'.format(i))
                else:
                    print('{:d}'.format(i), end=" ")
