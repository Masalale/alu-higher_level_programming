#!/bin/bash
# Checks what HTTP methods the server allows using OPTIONS request
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
