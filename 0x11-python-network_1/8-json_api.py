#!/usr/bin/python3
""" This script:
    1. Takes an alphabet/letter as input(commandline argument).
    2. Sends a POST request to the server in this machine with
    the letter as parameter.
    3. If the response body is properly JSON formatted and not
    empty, it displays the `id` and `name` in this format `[<id>] <name>`
    4. Does all the above using the Python requests library package
"""
import requests
import sys


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) != 2:
        query = ""
    else:
        query = sys.argv[1]

    param = {'q': query}

    response = requests.post(url, data=param)

    # Check if the response body is a JSON string
    try:
        # Parse response body as JSON string, returns
        # a Python dictionary if response body is a JSON string
        # otherwise a JSONDecodeError when it's not
        dict_repr = response.json()

        # If the JSON string is empty -> '{}'
        if dict_repr == {}:
            print('No result')
        else:
            # If it has content
            print('[{}] {}'.format(dict_repr.get('id'), dict_repr.get('name')))

    except Exception as e:  # Not a valid JSON
        print('Not a valid JSON')
