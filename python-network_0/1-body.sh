#!/bin/bash
# Gets the body of a 200 response - fails silently if not 200 OK
curl -sfL "$1" -X GET
