#!/usr/bin/python3
"""Sends a request to the passed URL and displays the response body.
if the HTTP status code is greater than or equal to 400, print
'Error code: ' followed by the value of the HTTP status code
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
