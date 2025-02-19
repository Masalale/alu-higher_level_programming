#!/usr/bin/python3
def no_c(str_in):
    str_out = ''
    for ch in str_in:
        if ch != 'c' and ch != 'C':
            str_out += ch
    return str_out
