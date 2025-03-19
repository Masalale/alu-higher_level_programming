#!/usr/bin/python3
"""
Python script that sends a POST request with a letter parameter
and handles the JSON response
"""
import requests
import sys


if __name__ == "__main__":
    # Set the letter parameter (q) - empty string if no argument provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # URL to send the POST request to
    url = "http://0.0.0.0:5000/search_user"
    
    # Send POST request with the letter as parameter
    r = requests.post(url, data={'q': q})
    
    # Try to parse the JSON response
    try:
        response_json = r.json()
        
        # Check if the JSON response is empty
        if response_json:
            print("[{}] {}".format(response_json.get('id'), response_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
