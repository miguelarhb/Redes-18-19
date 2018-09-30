#!/usr/bin/env python

import socket

TCP_IP = socket.gethostbyname("tejo.tecnico.ulisboa.pt")
TCP_PORT = 58011
BUFFER_SIZE = 1024
MESSAGE = "login 67890 aaaaaaaa"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
