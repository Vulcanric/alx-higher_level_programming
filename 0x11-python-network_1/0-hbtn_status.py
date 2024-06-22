#!/usr/bin/python3
""" This module uses the `urllib` Python library to retrieve a resource
from a URL
"""
import urllib

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    req = __import__('urllib.request').request

    with req.urlopen(url) as response:
        body = response.read()  # Response is a file object
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)  # body in byte b''
        print('\t- utf8 content:', body.decode())  # UTF-8 representation ''
