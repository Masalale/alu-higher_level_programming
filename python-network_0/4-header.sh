#!/bin/bash
# Makes a GET request with a custom user ID header to identify the client
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
