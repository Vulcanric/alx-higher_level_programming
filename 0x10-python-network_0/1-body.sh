#!/bin/bash
### Sends a GET request to URL passed as argument, and displays the body of the response
curl -L -X 'GET' "$1"
