    #!/usr/bin/env python
    
import socket
import sys
import datetime
import os


    
TCP_IP = "tejo.tecnico.ulisboa.pt"
TCP_PORT = 58011
BUFFER_SIZE = 128

class files(object):
    
    def __init__(self, name=None, date=None, size=None):
        self.name = name
        self.date = date
        self.size = size


def check_ip(data):
  lenght=len(data)
  words=0
  ip_sup=""
  for e in range(0,lenght):
    
    if(data[e]==" "):
      words+=1
    elif(words==1 and data[e]!=" "):
      ip_sup+=data[e]
  return ip_sup

def check_port(data):
  lenght=len(data)
  words=0
  port_sup=""
  for e in range(0,lenght):
  
    if(data[e]==" "):

      words+=1
    elif(words==2 and data[e]!=" "):
      port_sup+=data[e]
  return port_sup


#MESSAGE = b'AUT 67890 aaaaaaaa' 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
user=""
password=""
command_log=''


'''def check_login():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((TCP_IP, TCP_PORT))
  command_log='AUT'+' '+user+' '+password+'\n'

  command_send_bit=command_log.encode() 
  s.send(command_send_bit)
  data=s.recv(BUFFER_SIZE).decode()
  if(data=='AUR OK\n'):
    return True
  else:
    return False
'''


a=1;

while(a==1):

  MESSAGE=input();
  command_recv=""
  command_send=""
  
  directory=""
  palavra=0
  N=""
  ip=""
  port=""
  name=""
  date=""
  size=""
  filelist=[]
  lenght=len(MESSAGE)
  for i in range(0,lenght):
    if (MESSAGE[i]!=" " and palavra==0) :
      command_recv+=MESSAGE[i]
    elif(MESSAGE[i]==" "):
      #if(palavra==5 and command_recv=="backup"):


      palavra+=1

    elif(command_recv=="login" and palavra==1):
      user+=MESSAGE[i]
    elif(command_recv=="login" and palavra==2):
      password+=MESSAGE[i]
    elif((command_recv=="backup" or command_recv=="restore" or command_recv=="filelist" or command_recv=="delete") and palavra==1):
      directory+=MESSAGE[i]
    '''elif(command_recv=="backup" and palavra>=2):
      if(palavra==2):
        N+=MESSAGE[i]
      elif(palavra==3):
        name+=MESSAGE[i]
      elif(palavra==4):
        date+=MESSAGE[i]
      elif(palavra==5):
        size+=MESSAGE[i]'''


  if(command_recv=="login" ):
    command_send='AUT'+' '+user+' '+password+'\n'
    command_log='AUT'+' '+user+' '+password+'\n'
    command_send_bit=command_send.encode()  

    s.send(command_send_bit)
    data = s.recv(BUFFER_SIZE)
    print ( data.decode())
    s.close()

#COMMAND DELETE USER
  if(command_recv=="deluser"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command_log='AUT'+' '+user+' '+password+'\n'

    command_send_bit=command_log.encode() 
    s.send(command_send_bit)
    data=s.recv(BUFFER_SIZE).decode()
    if(data=='AUR OK\n'): 

      command_send='DLU '+'\n'
      command_send_bit=command_send.encode()
      s.send(command_send_bit)
      data=s.recv(BUFFER_SIZE)
      print(data.decode())
    s.close()

#COMMAND BACKUP
  if(command_recv=="backup"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command_log='AUT'+' '+user+' '+password+'\n'

    command_send_bit=command_log.encode() 
    s.send(command_send_bit)
    data=s.recv(BUFFER_SIZE).decode()

    if(data=='AUR OK\n'):
      files=os.listdir(directory)
      print(len(files))




    s.close()

#COMMAND RESTORE
  if(command_recv=="restore"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command_log='AUT'+' '+user+' '+password+'\n'

    command_send_bit=command_log.encode() 
    s.send(command_send_bit)
    data=s.recv(BUFFER_SIZE).decode()

    if(data=='AUR OK\n'):
      command_send='RST '+directory+'\n'
      command_send_bit=command_send.encode()
      s.send(command_send_bit)
      data = s.recv(BUFFER_SIZE)
      ip=check_ip(data.decode())
      port=check_port(data.decode())
      s.close()

      fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      fd.connect((ip, int(port)))

      command_send='AUT'+' '+user+' '+password+'\n'
      command_send_bit=command_send.encode()
      fd.send(command_send_bit)
      
      data = fd.recv(BUFFER_SIZE)

      if(data.decode()=='AUR OK\n'):

        command_send='RSB '+directory+'\n'
        command_send_bit=command_send.encode()
      
        fd.send(command_send_bit)
        space=0
        N=''
        decode_data=''
        img_name=''
        img_size=''
        while True:
        	if(space!=6):
        		data=fd.recv(1)
        	if not data:
        		break
        	if(data==b' '):
        		space+=1
        		data=data.decode()
        	elif(space==0 and data!=b' '):
        		data=data.decode()
        	elif(space==1 and data!=b' '):
        		N+=data.decode()
        		data=data.decode()
        	elif(space==2 and data!=b' '):
        		img_name+=data.decode()
        		data=data.decode()
        	elif((space==3 or space==4)and data!=b' '):
        		data=data.decode()
        	elif(space==5 and data!=b' '):
        		img_size+=data.decode()
        		data=data.decode()
        	elif(space==6):
        		print(img_size)
        		img_data=fd.recv(int(img_size))
			                                     
				
        		space=1
        	print(data,end='')
      fd.close()	

    

#COMMAND DIRLIST
  if(command_recv=="dirlist"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command_log='AUT'+' '+user+' '+password+'\n'

    command_send_bit=command_log.encode() 
    s.send(command_send_bit)
    data=s.recv(BUFFER_SIZE).decode()
    if(data == 'AUR OK\n' ):

      command_send='LSD'+'\n'
      #command_send_bit=command_send.encode()
      s.send(command_send.encode())
      while True:
        data = s.recv(1).decode('UTF8')
   
        if not data:
          break    # socket closed, all data read
        print(data, end='')

    
    s.close()
     
#COMMAND FILELIST
  if(command_recv=="filelist"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command_log='AUT'+' '+user+' '+password+'\n'

    command_send_bit=command_log.encode() 
    s.send(command_send_bit)
    data=s.recv(BUFFER_SIZE).decode()
    if(data=='AUR OK\n'):
      command_send='LSF '+directory+'\n'
      command_send_bit=command_send.encode()
      s.send(command_send_bit)
      while True:
        data = s.recv(10).decode('UTF8')
        if not data:
          break    # socket closed, all data read
        print(data, end='')

    s.close()
#COMMAND DELETE  
  if(command_recv=="delete"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    command_log='AUT'+' '+user+' '+password+'\n'

    command_send_bit=command_log.encode() 
    s.send(command_send_bit)
    data=s.recv(BUFFER_SIZE).decode()
    if(data=='AUR OK\n'):
      command_send='DEL '+directory+'\n'
      command_send_bit=command_send.encode()
      s.send(command_send_bit)
      data=s.recv(BUFFER_SIZE)
      print(data.decode())
    s.close()


  if(command_recv=="logout" ):
    user=''
    password=''
    command_log=''

  if(command_recv=="exit"):
    print("quero sair")
    a=0

  
  

  




