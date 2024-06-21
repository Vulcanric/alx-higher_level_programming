#!/usr/bin/python3
""" This module uses the `urllib` library to retrieve a responce header
    from a URL
"""
import urllib
import sys


if __name__ == "__main__":

    request = __import__('urllib.request').request

    url_ = sys.argv[1]  # Receives the URL as commandline argument
    with request.urlopen(url_) as resp:
        # Display the response header variable, 'X-Request-Id'

        print(resp.headers['X-Request-Id'])
