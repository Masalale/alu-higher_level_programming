#!/usr/bin/python3
"""
Python script that takes GitHub credentials and uses the GitHub API
to display the user's ID
"""
import requests
import sys


if __name__ == "__main__":
    # Get GitHub username and personal access token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]
    
    # GitHub API URL to get user information
    url = "https://api.github.com/user"
    
    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))
    
    # Parse the JSON response and display user ID
    json_data = response.json()
    print(json_data.get('id'))
