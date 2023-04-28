#!/bin/bash
#A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sSL -w '%{http_code}' "$1" | [ "$(tail -n 1)" == "200" ] && curl -s "$1"
