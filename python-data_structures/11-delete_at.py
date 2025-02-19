#!/usr/bin/python3
def delete_at(lst=[], i=0):
    if i < 0 or i > len(lst) - 1:
        return lst
    else:
        del lst[i]
        return lst
