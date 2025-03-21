#!/usr/bin/python3
"""
Script to get the X-Request-Id header value
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
