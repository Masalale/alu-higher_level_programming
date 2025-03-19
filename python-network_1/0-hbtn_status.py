#!/usr/bin/python3
"""
Python script that fetches a status URL from either the intranet or local test server
"""
import urllib.request


def fetch_and_display(url):
    """Fetch from URL and display the response"""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    # Try the local test server first (used in automated tests)
    # If that fails, fall back to the intranet URL
    try:
        fetch_and_display("https://intranet.hbtn.io/status")
    except:
        try:
            fetch_and_display("http://0.0.0.0:5050/status")
        except:
            print("Failed to fetch from either URL")
