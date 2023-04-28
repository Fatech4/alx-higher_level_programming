#!/bin/bash
#Sends a request to that URL, and disp the size of the body of the response
echo $(curl -sSL -w "%{size_download}" -o /dev/null "$url")
