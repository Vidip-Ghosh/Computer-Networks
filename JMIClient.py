import socket

c = socket.socket()

c.connect(('localhost',8888))

name = input("Enter your Name: ")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())

c.close()