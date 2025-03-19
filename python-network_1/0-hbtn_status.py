#!/usr/bin/python3
"""
Python script that fetches a status URL
"""
import urllib.request
import sys


if __name__ == "__main__":
    # Use provided URL or default to the original URL
    url = sys.argv[1] if len(sys.argv) > 1 else "https://alu-intranet.hbtn.io/status"
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
