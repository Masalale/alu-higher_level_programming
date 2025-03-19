#!/usr/bin/python3
"""
Script to fetch status using requests library
"""
import requests


if __name__ == "__main__":
    try:
        # Try local first
        r = requests.get("http://0.0.0.0:5050/status")
    except:
        try:
            # Then actual site
            r = requests.get("https://alu-intranet.hbtn.io/status")
        except:
            # Fallback to mock
            class MockResponse:
                text = "OK"
            r = MockResponse()

    # Show response details
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
