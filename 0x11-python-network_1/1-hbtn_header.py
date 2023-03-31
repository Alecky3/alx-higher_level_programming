#!/usr/bin/python3
"""Sends a request to URL and displays the value of the 'X-Request-Id'
   variable found in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(req.headers).get('X-Request-Id'))
