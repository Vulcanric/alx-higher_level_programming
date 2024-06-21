#!/usr/bin/python3
""" This module uses the `urllib` Python library to retrieve a resource
from a URL
"""
import urllib.request

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)                 # body is type 'byte' by default
        print('\t- utf8 content:', body.decode())   # Default encoding is utf-8
