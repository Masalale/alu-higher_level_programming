#!/usr/bin/python3
"""
Script to search for users with a given letter
"""
import requests
import sys
if __name__ == "__main__":
    # Get search term or use empty
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    # Server endpoint
    url = "http://0.0.0.0:5000/search_user"
    # Post the search term
    r = requests.post(url, data={'q': q})
    # Handle response
    try:
        response_json = r.json()
        # Check if we got results
        if response_json:
            print("[{}] {}".format(
                response_json.get('id'),
                response_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
