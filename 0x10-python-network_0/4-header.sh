#!/bin/bash
### Sends a HTTP 'GET' request with header 'X-School-User-Id: 98' to the given URL
curl -sX 'GET' -H 'X-School-User-Id: 98' "$1"
