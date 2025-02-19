#!/usr/bin/python3
def search_replace(input_list, search, replace):
    return [replace if x == search else x for x in input_list]
