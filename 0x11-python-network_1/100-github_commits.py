#!/usr/bin/python3
""" This script works with the GitHub API in the following ways:
    1. Takes a GitHub repository name and owner's name as input
    2. Lists 10 commits from the most recent to the oldest
    It does all these using the `requests` library package
"""
import requests
import sys


if __name__ == "__main__":
    # Get repository information
    repo = sys.argv[1]
    owner = sys.argv[2]

    # Set headers necessary for listing commits
    header = {'Accept': "application/vnd.github+json"}

    # Set path to users repository's commit
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url, headers=header)
    commits = response.json()  # Returns a list object - a list of all commits

    commit_count = min(len(commits), 10)  # Get 10 latest commits or less

    for i in range(commit_count):
        print(commits[i].get('sha'), end=': ')
        print(commits[i].get('commit').get('author').get('name'))
