#!/usr/bin/python3
""" This script does the following:
1. Takes a URL and an email address as input.
2. Sends a POST request to the passed URL with the email as a parameter
3. Finally displays the body of the response
 Does all the above using the `requests` package
"""
import requests
import sys


if __name__ == "__main__":
    # Retrieve URL and email address
    url = sys.argv[1]
    email = sys.argv[2]

    # Set email parameter
    parameter = {'email': email}

    # Send post request and print response
    response = requests.post(url, data=parameter)
    print(response.text)
