import socket
import struct
import sys

MULTICAST = "224.1.1.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

sock.bind((MULTICAST,PORT))

group = socket.inet_aton(MULTICAST)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


while True:
    data=sock.recv(1024)
    uid, message = data[0:6].decode(), data[6:].decode()
    print(message)

