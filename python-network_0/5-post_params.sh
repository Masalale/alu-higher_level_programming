#!/bin/bash
# Submits form data using POST with email and subject parameters and custom header
curl -s -X POST -H "X-HolbertonSchool-User-Id: 98" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
