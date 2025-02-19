#!/usr/bin/python3
def print_matrix_integer(mtx=[[]]):
    for r in mtx:
        for c in r:
            print("{:d}".format(c), end=" " if c != r[-1] else "")
        print()
