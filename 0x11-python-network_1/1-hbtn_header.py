#!/usr/bin/python3
import urllib.request
import sys
""" A module that sent a request and print the value of a header attribute"""
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.info()
    x_request_id = header['X-Request-Id']

print(x_request_id)
