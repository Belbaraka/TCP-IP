import socket
import struct
import sys

MULTICAST = "224.1.1.1"
PORT = 5005

message = "245846 This is my first message"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

sock.sendto(message.encode(), (MULTICAST,PORT))
sock.close()   
