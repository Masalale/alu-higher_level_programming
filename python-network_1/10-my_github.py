#!/usr/bin/python3
"""
Script to get GitHub user ID using credentials
"""
import requests
import sys
if __name__ == "__main__":
    # Get auth info from args
    username = sys.argv[1]
    token = sys.argv[2]
    # API endpoint
    url = "https://api.github.com/user"
    # Make authenticated request
    response = requests.get(url, auth=(username, token))
    # Extract and print user ID
    json_data = response.json()
    print(json_data.get('id'))
