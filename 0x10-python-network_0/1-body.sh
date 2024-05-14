#!/bin/bash
### Sends a GET request to URL passed as argument, and displays the body of the response
curl -sL -X 'GET' "$1"
