import socket
import sys
import os
from datetime import datetime
from BS_commands import *

UDP_IP = "192.168.1.187"
UDP_PORT = 58008
user = ""

BUFFER_SIZE = 1024
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))



#REG_protocol(sock, UDP_IP, UDP_PORT, BUFFER_SIZE)
#print(data)
#get_newest_folder("BS/00000")   
while True:

  data, address = sock.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes
  message = data
  data_decoded = message.decode()
  parameters = data_decoded.split()
  stuff = verify_args(data_decoded)

  if(len(stuff) == 3):
  	if(equal_code(stuff[0], "LSF")):
  		print("CENAS, WHY NOT")
  		send_message = LSF_protocol(stuff[0], stuff[1], stuff[2])
  		message = send_message.encode()
  		print(message)
  		#print(address)
  		sock.sendto(message, address)
sock.close()  		




print("received message:", data_decoded)

