#!/usr/bin/python3
""" A module that send a get request to https://alx-intranet.hbtn.io/status"""
if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", decoded_body)
