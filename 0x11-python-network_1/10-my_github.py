#!/usr/bin/python3
""" This script:
    1. Takes GitHub credentials of a user as input
    2. then uses the GitHub API to display the user's id
    It does all the above using the Python `requests` package
"""
import requests
import sys


if __name__ == "__main__":
    # Get GitHub credentials
    user = sys.argv[1]  # User's GitHub username
    token = sys.argv[2]  # User's Personal Access Token

    url = 'https://api.github.com/users/' + user

    # Set authorization header
    header = {'Authorization': "Bearer " + token}

    response = requests.get(url, headers=header)
    # Convert JSON string to Python dictionary of user @user
    user = response.json()
    print(user.get('id'))
