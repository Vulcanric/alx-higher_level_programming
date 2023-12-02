#!/usr/bin/python3
""" This module uses the `urllib` library to fetch resources from the URL
'https://alx-intranet.hbtn.io/status'
"""
import urllib.request


if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as resp:
        body = resp.read()                  # Body content
        print('Body response:')
        print(f"\t- type: {body.__class__}")    # type(body)
        print(f"\t- content: {body}")           # Body's content in byte b''
        print(f"\t- utf8 content: {resp.msg}")  # UTF-8 representation ''
