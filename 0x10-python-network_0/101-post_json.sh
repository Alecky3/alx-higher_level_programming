#!/bin/bash
# Sends a JSON POST request and displays the body of the response
curl -s -H "Content-Type: application/json" -X POST -d "$(cat "$2")" "$1"
