#!/bin/bash
# Makes a GET request with a custom user ID header to identify the client
curl -sL -H "X-HolbertonSchool-User-Id:98" "$1"
