#!/bin/bash
# Script that displays the body of a 200 status code response
curl -sfL "$1" -X GET
