import socket
import re

def server_program():

    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:

        data = conn.recv(1024).decode()
        if not data:
            break
        if re.search('^[a-zA-Z0-9_]+$',data):
            print('Found Alphanumeric characters')
        elif re.search("[!@#$%^&*()]+$",data):
            print('Found Special Characters')
        else:
            print('Not Found')
        
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()