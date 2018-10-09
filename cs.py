#!/usr/bin/env python
import socket
import os
from CS_commands import *

user = ""
bck = ""
TCP_IP = "192.168.1.187"
TCP_PORT = 5005
UDP_IP = "192.168.1.187"
UDP_PORT = 58008

BUFFER_SIZE = 20  # Normally 1024, but we want fast response


'''sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
data, addr  =sock.recvfrom(1024)
data_decoded = data.decode()
parameters = data_decoded.split(' ')
print(data_decoded)
print(len(parameters))
if(len(parameters) == 3):
	print(equal_code(parameters[0], "REG"))
	if(equal_code(parameters[0], "REG")):
		print("SERA QUE VOU ENVIAR RGR?")
		send_message = REG_protocol(sock, parameters[1], parameters[2])
		print("OLHA SO, SAI DO PROTOCOLO")
		print(send_message)
		sock.sendto(send_message.encode(), (UDP_IP, UDP_PORT))'''



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print('Connection address:', addr)
word = ""
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data.decode())
    dir_path = os.path.dirname(os.path.realpath(__file__))
    string = data.decode()
    print(data)
    parameters = string.split()
    if(len(parameters)==3 and parameters[0] != "REG"):
    	code = parameters[0]
    	user = parameters[1]
    	password = parameters[2]
    	poss_dir_path = dir_path + "/" + user

    if(len(parameters)==3 and parameters[0] == "REG"):
    	code = parameters[0]
    	ip = parameters[1]
    	port = parameters[2]

    elif(len(parameters)==2):
    	code = parameters[0]
    	diret = parameters[1]

    elif(len(parameters)==1):
    	code = parameters[0]

    
    if(code == "AUT" and os.path.isfile("CS/user_" + user + ".txt") == False):
    	save_path = "CS/"
    	completeName = os.path.join(save_path, "user_" + user + ".txt")   
    	f = open(completeName, "w+")
    	f.write(user + " " + password)
    	f.close()
    	check = "AUR NEW"
    	conn.send(check.encode())  # echo

    elif(code == "AUT" and os.path.isfile("CS/user_" + user +".txt") == True):
    	print("ENTREI")
    	filepath = "CS/user_" + user + ".txt"
    	with open(filepath) as fp:
    		line = fp.readline()
    		user_data, password_data = line.split()
    	if(password_data == password):
    		check = "AUR OK\n"
    	else:
    		check = "AUR NOK"
    	conn.send(check.encode())  # echo

    elif(code == "DLU" and os.path.isfile("CS/" + user+".txt") == True):
    	print(user, "is defined")
    	new_dir = dir_path + "/CS/" + user 
    	if(os.path.isdir(new_dir)):
    		check = "DRL NOK"
    	else:
    		os.remove(user+".txt")
    		check = "DLR OK"
    	conn.send(check.encode())

    elif(code=="LSD"):
    	print("ENTREI BOI")
    	dirs = ""
    	new_dir = dir_path + "/CS/" + user
    	print(os.path.isdir(new_dir))
    	if(os.path.isdir(new_dir)):
    		files = os.listdir(new_dir)
    		print(files)
    		for name in files:
    			dirs += name + " "
    			print(dirs)
    		if(dirs == ""):
    			check ="LDR" + " " + "0"
    			conn.send(check.encode())
    		else:
    			check = "LDR" + " " + dirs + "\n"
    			print(check)
    			conn.send(check.encode())
    	else:
    		check = "LDR NOK"
    		conn.send(check.encode())    		

    	#if(os.path.dirname(os.path.realpath(__file__)))

    elif(code == "LSF"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        send_command_string = "LSF " + user +" " + diret
        send_command = send_command_string.encode()
        sock.sendto(send_command, (UDP_IP, UDP_PORT))

        while True:
            data, address = sock.recvfrom(BUFFER_SIZE)
            if not data:
                break
            print(data, end='')
        sock.close()
    	
        message = data[0]
        data_decoded = message.decode()
        parameters = data_decoded.split()
        send_command = parameters[0] + " " + UDP_IP + str(UDP_PORT)
        for i in range(1, len(parameters)):
            send_command += " " + parameters[i]

        print(send_command)

  	#elif(code == "DEL"):



conn.close()

'''UDP_IP = "192.168.1.101"
UDP_PORT = 5005
MESSAGE = "Hello, World!"
 
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)
 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
MESSAGE_BIT = MESSAGE.encode()
sock.sendto(MESSAGE_BIT, (UDP_IP, UDP_PORT))'''
