#!/usr/bin/python3
def element_at(lst, i):
    if i < 0 or i > len(lst) - 1:
        return None
    else:
        return lst[i]
