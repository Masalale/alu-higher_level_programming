#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    total = 0
    last_value = 0
    for numeral in reversed(roman_string):
        current_value = roman_numerals.get(numeral, 0)
        if current_value >= last_value:
            total += current_value
        else:
            total -= current_value
        last_value = current_value
    return total
