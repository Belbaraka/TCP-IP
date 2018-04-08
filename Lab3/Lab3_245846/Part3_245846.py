import socket
import re
import sys

HOST = "lab3.iew.epfl.ch"
PORT = 5004
command="RESET:20"
ack_formatlen=len("OFFSET=10")

response = re.compile('OFFSET:\d+')

def send(cmd):
    socket_type=socket.AF_INET

    while True:
        try:
            sock=socket.socket(socket_type,socket.SOCK_DGRAM)
            sock.settimeout(1)

            sock.sendto(cmd.encode(),(HOST, PORT))
            data, _= sock.recvfrom(ack_formatlen)

            sock.close()
            return data.decode()

        except socket.timeout as error:
            print(error)
            if socket_type==socket.AF_INET:
                socket_type=socket.AF_INET6
            else:
                socket_type=socket.AF_INET
            sock.close()

        except OSError as error:
            print(error)
            if socket_type==socket.AF_INET:
                socket_type=socket.AF_INET6
            else:
                socket_type=socket.AF_INET
            sock.close()



received = None
while not received:
    val=send(command)
    print(val)
    received=response.match(val)
    
