#!/usr/bin/python3
"""script that fetches alu-intranet.hbtn.io status using urllib"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
        body_res = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_res)))
        print("\t- content: {}".format(body_res))
        print("\t- utf8 content: {}".format(body_res.decode("utf-8")))
