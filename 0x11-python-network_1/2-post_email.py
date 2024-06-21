#!/usr/bin/python3
""" Sends a POST request to the server specified by URL with
a parameter: email
"""
import urllib
import sys


if __name__ == "__main__":

    # Get info as commandline arguments
    url = sys.argv[1]
    email = sys.argv[2]

    request = __import__('urllib.request').request
    parse = __import__('urllib.parse').parse

    value = {'email': email}
    # Encode parameter
    param = parse.urlencode(value)  # Value becomes 'email=name@domain.com'
    param = param.encode('ascii')  # Convert string(param) to bytes b''

    with request.urlopen(url, data=param) as response:
        print(response.read().decode())
