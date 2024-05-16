#!/bin/bash
### Takes in a URL, retrieves and displays all the HTTP methods the server will accept
curl -siLX 'OPTIONS' "$1" | grep "Allow" | sed -e 's/Allow: //'
