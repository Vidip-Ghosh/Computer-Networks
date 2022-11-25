import socket


def decrypt(cipherText, s):
    result = ""
    for i in range(len(cipherText)):
        char = cipherText[i]
        if (char.isupper()):
            result += chr((ord(char)-s-65) % 26 + 65)
        else:
            result += chr((ord(char)-s-97) % 26 + 97)
    return result


def socket_program():
    host = socket.gethostname()
    port = 6300
    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("->")
    while message != 'bye':

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        key = input("Enter key to receive decrypted message from server:-> ")
        key = int(key)
        s = data[-1]
        s = int(s)
        text = data[:-1]
        text = str(text)
        print(s)
        if (key == s):
            print("Decrypted text: " + decrypt(text, s))
            message = input('->')
        else:
            print("wrong key entered, terminating program")
            break
        client_socket.close()


if __name__ == "__main__":
    socket_program()
