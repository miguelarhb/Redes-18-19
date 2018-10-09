#BS FUNCTIONS

import socket
import sys
import os
import glob
import os
from datetime import datetime

def verify_args(string):

	parameters = string.split(' ')
	if(len(parameters)==3 and parameters[0]) != "LSF":
		code = parameters[0]
		user = parameters[1]
		password = parameters[2]
		return code, user, password

	elif(len(parameters) == 3 and parameters[0] =="LSF"):
		code = parameters[0]
		user = parameters[1]
		diret = parameters[2]
		return code, user, diret

	elif(len(parameters)==2):
		code = parameters[0]
		diret = parameters[1]
		return code, diret

	elif(len(parameters)==1):
		code = parameters[0]
		return code

def accept_UDP_connection(socket, check):
	socket.recvfrom()

def equal_code(command, string):
	if(command == string):
		return True
	return False

def get_newest_folder(directory):
	folder = max(glob.glob(os.path.join(directory, "*/")), key=os.path.getmtime)
	print(folder)
	return folder

def REG_protocol(socket, UDP_ip, UDP_port, buff):
	check = "REG " + UDP_ip + " " + str(UDP_port)
	socket.sendto(check.encode(), (UDP_ip, UDP_port))
	print("Enviei cenas")
	while True:
		print("FODASSE CARALHO")
		data = socket.recvfrom(buff)
		print("recebi")
		if not data:
			break
		print(data, end='')

def LSF_protocol(code, user, diret):
	path = "BS/" + user + "/" + diret
	if(os.path.isdir(path)):
   		num_files = len(os.listdir(path))
   		check = "LFD " + str(num_files) + " "
   		for files in os.walk(path, topdown=False):
   			file_name = files[2]
   			file = file_name[0]
   			time = os.path.getmtime(path +"/" + file)
   			date_time= datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')
   			size = os.path.getsize(path +"/" + file)
   			check += file + " " + date_time + " " + str(size)
   			#print(files)
   			print(check)
   		return check



