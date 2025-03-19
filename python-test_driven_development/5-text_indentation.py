#!/usr/bin/python3
"""
Text indentation module - provides a function to format text with new lines
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':' character
    
    Args:
        text: Input string to process
        
    Raises:
        TypeError: If text is not a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Process the text character by character
    i = 0
    
    # Skip initial spaces
    while i < len(text) and text[i] == ' ':
        i += 1
    
    # Process each character
    while i < len(text):
        print(text[i], end="")
        
        # Add two newlines after special characters
        if text[i] in ".?:":
            print("\n\n", end="")
            i += 1
            # Skip spaces after special characters
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
