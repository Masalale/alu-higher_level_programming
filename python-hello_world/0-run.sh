#!/bin/bash

# Check if PYFILE is set
if [ -z "$PYFILE" ]; then
  echo "Error: PYFILE environment variable is not set."
  exit 1
fi

# Run the Python script
python "$PYFILE"