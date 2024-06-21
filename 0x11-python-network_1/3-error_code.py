#!/usr/bin/python3
""" This module uses the `urllib` library to retrieve a responce header
    from a URL
"""
import urllib
import sys


if __name__ == "__main__":

    url = sys.argv[1]  # Receives the URL as a commandline argument

    request = __import__('urllib.request').request

    try:
        with request.urlopen(url) as response:
            print(response.read().decode())  # Response body decoded in UTF-8
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
