import socket
server_socket = socket.socket()
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5)

while True:
    print("Server waiting for connection")
    client_socket, addr=server_socket.accept()
    print("Client connected from",addr)
    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break
        c=data.encode('utf-8')
        print("Received from client: " + c)
        try:
            client_socket.send(bytes('Hey client','utf-8'))
        except:
            print('Exited by the user')
    client_socket.close()
server_socket.close()