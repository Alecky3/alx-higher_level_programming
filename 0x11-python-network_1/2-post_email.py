#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as parameter
   and dislays the body of the response(decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
