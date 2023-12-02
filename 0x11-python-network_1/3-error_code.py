#!/usr/bin/python3
""" This module uses the `urllib` library to retrieve a responce header
    from a URL
"""
import sys
import urllib


if __name__ == "__main__":

    request = __import__('urllib.request').request

    url_ = sys.argv[1]  # Receives the URL as commandline argument
    with request.urlopen(url_) as resp:

        print(resp.msg)
        print("Error code: {resp.code}")
