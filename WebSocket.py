"""
WebSocket.py

Created on Thurs Oct 5 12:45:37 2023

@author: Mark Graham
"""
import socket
import sys

### Understanding the code

## Setup an exception just in case the connection doesn't work.
try:

## AF_INET = IPv4 (Internet Protocol version 4) [the dominate protocol]
## SOCK_STREAM = Establish TCP (Transmission Control Protocol)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket creation successful!')

## Receives the error code and displays if for debugging purposes.
except socket.error as err:
    print(f'Socket creation failed. Error code: {err}')

## Sets the main port to 80 also know as the Network port that
## commonly uses HTTP (Hypertext Transfer Protocol).
port = 80

## Gets the IP address of Github's main website.
try:
    host_ip = socket.gethostbyname('www.github.com')

## If failed, then stops application and produces the error below.
except socket.gaierror:
    print('Error resolving the host!')
    sys.exit()

## Connects the socket to Github and displays the proper IP address
## github with a confirmation message.
server.connect((host_ip, port))
print(f'Socket has successfully connect to GitHub on port {host_ip}.')