import socket


def encryptRailFence(message, key):

    key = int(key)

    rail = [['\n' for i in range(len(message))]
            for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(message)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = message[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(message)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("" . join(result))


def client_program():
    host = socket.gethostname()
    port = 7500

    client_socket = socket.socket()

    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        print("enter key: ")
        key = input()
        print(encryptRailFence(message, key))
        encrypted = encryptRailFence(message, key)
        client_socket.send(encrypted.encode())
        client_socket.send(key.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)

        message = input(" -> ")
    client_socket.close()


if __name__ == '__main__':
    client_program()
