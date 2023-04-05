#!/bin/bash
# show all https request methods accepted by a server
curl -sI $1 | grep Allow | cut -d' ' -f 2-
