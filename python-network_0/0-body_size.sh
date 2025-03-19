#!/bin/bash
# Script that displays the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length
