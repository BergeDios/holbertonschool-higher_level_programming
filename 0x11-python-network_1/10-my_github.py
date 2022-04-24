#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user/{}'.format(sys.argv[1])
    password = sys.argv[2]
    header = {"Authorization" : "Basic {}".format(password)}
    r = requests.get(url, headers=header)
    print(r.json().get('id'))
