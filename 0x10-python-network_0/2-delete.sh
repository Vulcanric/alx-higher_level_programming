#!/bin/bash
### Sends a DELETE request to a server identified by the URL passed as an argument
curl -sLX "DELETE" "$1"
