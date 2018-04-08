import socket
import sys

HOST = "tcpip.epfl.ch"
PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

command0="CMD_short:0"
command1="CMD_short:1"

command_flood="CMD_floodme"

# uncomment which command to send

#sock.sendall(command0encode()) 
#sock.sendall(command1.encode())
sock.sendall(command_flood.encode())


size_buff=len("This is PMU data x")

unknown_size=200
number_of_times=0
while True:
    #data=sock.recv(size_buff).decode() #uncomment if command0 or command1 is used
    data =sock.recv(unknown_size).decode() #uncomment if command_flood is  used
    number_of_times+=1
    if data:
        print (data)
    else:
        break
print (number_of_times)      
sock.close()
