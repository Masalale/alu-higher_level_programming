#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves to a file
"""
import sys
import os.path

# Import functions from previous modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Create an empty list if file doesn't exist
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
