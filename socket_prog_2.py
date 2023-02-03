# example for connecting Google using socket programming in Python

import socket 
import sys

try:
    s=socket.socket (socket.AF_INET,socket.SOCK_STREAM)
    print("socket successfully created")
except socket.error as err:
    print("Socket creation failed with err: ",err)

# default port of socket 
port=80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server 
s.connect((host_ip,port))

print("Socket connected successfully with Google")


