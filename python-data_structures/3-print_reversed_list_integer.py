#!/usr/bin/python3
def print_reversed_list_integer(lst=[]):
    if lst:
        for n in lst[::-1]:
            print("{:d}".format(n))
