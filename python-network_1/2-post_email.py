#!/usr/bin/python3
"""
Script to POST email using urllib
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Format data for POST
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send request
    with urllib.request.urlopen(url, data=data) as response:
        # Get response
        body = response.read().decode('utf-8')
        print(body)
