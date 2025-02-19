#!/usr/bin/python3
def replace_in_list(lst, i, el):
    if i < 0 or i > len(lst) - 1:
        return lst
    else:
        lst[i] = el
        return lst
