import socket


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypting the uppercase letter
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypting the lowercase letter
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result


def socket_program():
    host = socket.gethostname()
    port = 6300
    socket_server = socket.socket()
    socket_server.bind((host, port))
    socket_server.listen(2)
    conn, add = socket_server.accept()
    print("ADDRESS: "+str(add))

    while True:
        data = conn.recv(1024).decode()
        print(data)
        data = input("->")
        s = input("enter key: ")
        s = int(s)
        print("Text : " + data)
        print("Shift : " + str(s))
        print("Cipher: " + encrypt(data, s))
        a = encrypt(data, s)
        s = str(s)
        a = str(a)
        data = a+s
        conn.send(data.encode())
        conn.close()


if __name__ == "__main__":
    socket_program()
