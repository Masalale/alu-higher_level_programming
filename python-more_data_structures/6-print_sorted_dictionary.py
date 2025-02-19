#!/usr/bin/python3
def print_sorted_dictionary(input_dict):
    for sorted_key in sorted(input_dict.keys()):
        print("{}: {}".format(sorted_key, input_dict[sorted_key]))
