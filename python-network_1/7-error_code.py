#!/usr/bin/python3
"""
Script to handle HTTP error codes
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    # Get URL content
    r = requests.get(url)
    # Check for error status
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        # Show content
        print(r.text)
