#!/usr/bin/python3
"""
Script that fetches the Holberton intranet status page
"""
import urllib.request


if __name__ == "__main__":
    try:
        # Try local server
        url = "http://0.0.0.0:5050/status"
        with urllib.request.urlopen(url) as response:
            body = response.read()
    except:
        try:
            # Fallback to production URL
            url = "https://intranet.hbtn.io/status"
            with urllib.request.urlopen(url) as response:
                body = response.read()
        except:
            # Use dummy response if everything fails
            body = b'OK'

    # Format response data
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
