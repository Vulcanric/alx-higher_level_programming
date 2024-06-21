#!/usr/bin/python3
""" This script:
    1. Takes a URL as input from commadline argument
    2. Sends a request(GET) to the URL
    3. And if there isn't any error, it displays the response body
    otherwise the error code as 'Error code: <ErrCode>'
    4. It does all the above using the Python `requests` package
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Detect if response is an error
    if response.status_code < 400:  # Not an error
        print(response.text)
    else:  # An error (4** to 5**)
        print('Error code:', response.status_code)
