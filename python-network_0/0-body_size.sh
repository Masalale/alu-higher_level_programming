#!/bin/bash
# Takes a URL, sends a request and returns the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
