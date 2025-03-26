#!/usr/bin/python3
"""send a POST request to the passed URL with the email as parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url_rs = sys.argv[1]
    email = sys.argv[2]
    rs = {"email": email}
    value = urllib.parse.urlencode(rs)
    value = value.encode('ascii')
    req = urllib.request.Request(url_rs, value)
    with urllib.request.urlopen(req) as res:
        body_res = res.read()
        print(body_res.decode('utf-8'))
