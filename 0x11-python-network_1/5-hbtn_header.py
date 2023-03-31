#!/usr/bin/python3
"""Sends a request to the passed URL and displays the value of the variable
   'x-Request-Id' in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
