#!/usr/bin/python3
"""sends a POST request to the passed URL
with the email as a parameter and display it"""

import requests
import sys

if __name__ == "__main__":
    url_res = sys.argv[1]
    email = sys.argv[2]
    val = {"email": email}
    response = requests.post(url_res, val)
    print(response.text)
