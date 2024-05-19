#!/bin/bash
### Sends a JSON POST request to a URL passed as the first argument and displays the body of response
curl -sX 'POST' -d @"$2" "$1"
