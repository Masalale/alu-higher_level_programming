#!/usr/bin/python3
"""
Python script that sends a request to a URL and displays the response body,
or prints the error code if status code >= 400
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    # Send GET request to the URL
    r = requests.get(url)
    
    # Check if the status code indicates an error
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        # Display the response body
        print(r.text)
