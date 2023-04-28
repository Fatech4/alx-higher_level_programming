#!/bin/bash
#A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sSL -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -sSL "$1"
