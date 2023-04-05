#!/bin/bash
# send POST request with header variables using curl
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
