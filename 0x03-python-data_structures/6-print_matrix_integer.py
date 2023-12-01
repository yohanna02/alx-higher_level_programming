#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            length = len(i) - 1
            idx = 0
            for j in i:
                print("{:d}".format(j), end="")
                if length != idx:
                    print(" ", end="")
                idx += 1
            print()
