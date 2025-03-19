#!/bin/bash
# Makes a GET request with a custom user ID header to identify the client
curl -sH "X-School-User-Id: 98" "$1"
