#!/usr/bin/python3
"""takes your GitHub credentials and display id"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    json_res = response.json()
    print(json_res.get('id'))
