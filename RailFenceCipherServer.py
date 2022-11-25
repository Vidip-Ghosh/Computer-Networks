import socket


def decryptRailFence(data, key):

    rail = [['\n' for i in range(len(data))]
            for j in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(data)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(data)):
            if ((rail[i][j] == '*') and
               (index < len(data))):
                rail[i][j] = data[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(data)):

        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))


def server_program():
    host = socket.gethostname()
    port = 7500

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("Enter key: ")
        authenticate = input()
        if (authenticate == data[len(data)-1]):
            print("from connected user: " + str(data))
            key = int(data[len(data)-1])
            data = data.rstrip(data[-1])
            print(decryptRailFence(data, key))

        else:
            print("Wrong key, Cannot access message")

        data = input(' -> ')
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    server_program()
