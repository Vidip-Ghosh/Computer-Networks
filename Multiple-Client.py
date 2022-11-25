import socket
from _thread import *

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connecction')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response2 = ClientSocket.recv(1024)
    print(Response2.decode('utf-8'))
ClientSocket.close()
