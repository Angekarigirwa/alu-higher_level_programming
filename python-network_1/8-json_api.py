#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    body_res = {'q': ""}
    if len(sys.argv) > 1:
        body_res['q'] = sys.argv[1]

    response = requests.post(url, body_res)
    try:
        data = response.json()
        if 'id' in data and 'name' in data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
