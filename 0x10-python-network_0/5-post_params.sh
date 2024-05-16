#!/bin/bash
### Sends a HTTP 'POST' request to the passed URL, along with a query string
curl -sX 'POST' -d 'email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD' "$1"
