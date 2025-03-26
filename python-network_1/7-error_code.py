#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the body of the response."""
import requests
import requests.exceptions
import sys

if __name__ == "__main__":
    try:
        response_r = requests.get(sys.argv[1])
        response_r.raise_for_status()
        print(response_r.text)
    except requests.exceptions.HTTPError as error:
        print("Error code: {}".format(error.response.status_code))
