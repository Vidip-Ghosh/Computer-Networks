import socket

s = socket.socket()        #s-> server socket c->client socket
print('Socket Created')

s.bind(('localhost',8888))

s.listen(3)     #How many connections are created
print('waiting for connection')

while True:
    c,addr = s.accept()      #Responsible for accepting the connection
    name = c.recv(1024).decode()
    print("Connected with ",addr,name)

    c.send(bytes('Vidip Ghosh','utf-8'))

    c.close()