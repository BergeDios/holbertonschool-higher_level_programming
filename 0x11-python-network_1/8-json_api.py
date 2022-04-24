#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except:
        pass

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        r_json = r.json()
        if not r_json:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except:
        print("Not a valid JSON")
