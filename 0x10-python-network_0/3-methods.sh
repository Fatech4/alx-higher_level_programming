#!/bin/bash
#A bash script that takes in a URL and display all HTTP methods the server will accept
curl -s -I "$1" | grep "Allow:" | cut -d " " -f 2-
