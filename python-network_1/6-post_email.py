#!/usr/bin/python3
"""
Script to POST an email address to a URL
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # Setup post data
    data = {'email': email}
    # Send request
    r = requests.post(url, data=data)
    # Show response
    print(r.text)
