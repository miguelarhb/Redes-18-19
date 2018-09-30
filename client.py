    #!/usr/bin/env python
    
import socket
import sys
    
TCP_IP = "tejo.tecnico.ulisboa.pt"
TCP_PORT = 58011
BUFFER_SIZE = 128
#MESSAGE = b'AUT 67890 aaaaaaaa' 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


user=""
password=""
command_log=''
a=1;
while(a==1):
  MESSAGE=input();
  command_recv=""
  command_send=""
  directory=""
  palavra=0
  lenght=len(MESSAGE)
  for i in range(0,lenght):
    if (MESSAGE[i]!=" " and palavra==0) :
      command_recv+=MESSAGE[i]
    elif(MESSAGE[i]==" "):
      palavra+=1
    elif(command_recv=="login" and palavra==1):
      user+=MESSAGE[i]
    elif(command_recv=="login" and palavra==2):
      password+=MESSAGE[i]
    elif((command_recv=="backup" or command_recv=="restore" or command_recv=="filelist") and palavra==1):
      directory+=MESSAGE[i]





  if(command_recv=="login"):
    command_send='AUT'+' '+user+' '+password+'\n'
    command_log='AUT'+' '+user+' '+password+'\n'
    command_send_bit=command_send.encode()  
    s.send(command_send_bit)

  elif(command_recv=="deluser"):
    command_send='DLU '+user+' '+password+'\n'

  #if(command_recv=="backup"):
    #do something

  elif(command_recv=="restore"):
    command_send='RST '+directory+'\n'
    command_send_bit=command_send.encode()
    s.send(command_send_bit)

  elif(command_recv=="dirlist"):
    print("entrei")
    command_send='LSD'+'\n'
    command_send_bit=command_send.encode()
    s.send(command_send_bit) 

  elif(command_recv=="filelist"):
    command_send='LSF'+directory+'\n'
    command_send_bit=command_send.encode()
    s.send(command_send_bit)


  data = s.recv(BUFFER_SIZE)
  print ( data.decode())

  if(command_recv=="exit"):
    print("quero sair")
    a=0

  
  

  

s.close()