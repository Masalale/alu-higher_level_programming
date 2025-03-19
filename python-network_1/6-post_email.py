#!/usr/bin/python3
"""
Python script that takes a URL and email address, sends a POST request with the email,
and displays the response body
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data for POST request
    data = {'email': email}
    
    # Send POST request and get response
    r = requests.post(url, data=data)
    
    # Display the response body
    print(r.text)
