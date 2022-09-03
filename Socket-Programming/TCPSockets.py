#creating a TCP Socket
import socket
import sys

#TCP Socket-> SOCK_STREAM, UDP Socket-> SOCK_DGRAM
try:
    s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create socket")
    print("Reason: "+str(err))
    sys.exit()
print("Socket is created")
target_host = input("Enter the target host: ")
target_port = input("Enter the target_port: ")

try:
    # s.connect(target_host,int(target_port))
    s.connect((target_host,int(target_port)))
    print("Socket Connected to: "+ target_port + target_host)
    # s.shutdown(2)
    
except socket.error as err:
    print("Failed to connect: "+ target_host + target_port)
    print("Reason: "+str(err))
    sys.exit()