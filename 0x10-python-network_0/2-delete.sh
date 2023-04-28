#!/bin/bash
#A Bash script that sends DELETE request to $1 and display the body of response
curl  -s -X DELETE "$1"
