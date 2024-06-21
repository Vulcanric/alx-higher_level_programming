#!/usr/bin/python3
"""Sends a request to a server specified by the URL and displays the value
of the variable `X-Request-Id` in the response header. This time, using the
`requests` package
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # Get URL from commandline
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
