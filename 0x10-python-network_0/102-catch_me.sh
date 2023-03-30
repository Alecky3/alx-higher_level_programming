#!/bin/bash
# Makes a request to 0.0.0.0:500/catch_me the causes server to respond with a message 'You got me'
curl -s -X PUT -H "Origin: HPElite-Bool" -d 'name=alex' 0.0.0.0:500/catch_me
