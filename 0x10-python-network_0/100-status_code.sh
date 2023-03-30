#!/bin/bash
# Sends a request to a URL, and displays only the status code for the response
curl -s -o /dev/null -w "%{http_code}" "$1"
