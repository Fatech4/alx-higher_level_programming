#!/bin/bash
# A bash script that takes in a URL as an argument, sends a GET request to the URL with a custom header, and displays the body of the response
curl -sSL -H "X-School-User-Id: 98" "$1"
