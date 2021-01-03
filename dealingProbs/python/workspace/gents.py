# import socket
#
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
import requests
import json

file = requests.get("http://data.pr4e.org/authors.txt")
print(file.text)