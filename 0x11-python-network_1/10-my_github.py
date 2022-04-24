#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, password))
    print(r.json().get('id'))
