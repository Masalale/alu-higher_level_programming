#!/usr/bin/python3
"""
Python script that fetches a status URL
"""
import urllib.request


if __name__ == '__main__':
    url = 'http://0.0.0.0:5050/status'
    
    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))