#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the body of the response"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            body_res = res.read()
            print(body_res.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))
