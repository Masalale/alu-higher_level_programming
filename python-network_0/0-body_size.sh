#!/bin/bash
# Script that displays the size of the response body in bytes

# Prepend "http://" if the URL doesn't start with http or https
if [[ $1 != http* ]]; then
  url="http://$1"
else
  url="$1"
fi

curl -s "$url" | wc -c
