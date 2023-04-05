#!/bin/bash
# send a POST request with a json file using curl
curl -s -H 'Content-Type: application/json' -d @$2 -X POST $1
