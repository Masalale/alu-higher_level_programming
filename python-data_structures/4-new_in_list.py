#!/usr/bin/python3
def new_in_list(lst, i, el):
    if i < 0 or i > len(lst) - 1:
        return lst
    else:
        new_lst = lst[:]
        new_lst[i] = el
        return new_lst
