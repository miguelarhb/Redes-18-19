#CS FUNCTIONS

import socket
import sys
import os
import glob
import os
from datetime import datetime

def REG_protocol(socket, ip, port):
	print("PROTOCOLO REG PENETRADO")
	if(os.path.isfile("CS/BS_list.txt")):
		save_path = "CS/"
		completeName = os.path.join(save_path, "BS_list.txt")
		file = os.path.basename(completeName)   
		f = open(completeName)
		line = f.readline()
		while line:
			#print(line)
			line = f.readline()
			data = line.split(' ')
			if(data[0] == ip and data[1] == port):
				check = "RGR ERR"
				PORT = int(port)
				return check
		f.close()
		f = open(completeName, "w")
		f.write(ip + " " + port + "\n")
		check = "RGR OK"
		PORT = int(port)
		print(PORT)
		return check

	elif(os.path.isfile("CS/BS_list.txt") == False):
		save_path = "CS/"
		completeName = os.path.join(save_path, "BS_list.txt")   
		f = open(completeName, "w")
		f.write(ip + " " + port + "\n")
		check = "RGR OK"
		print(check)
		PORT = int(port)
		return check

def equal_code(command, string):
	if(command == string):
		return True
	return False
