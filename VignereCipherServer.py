import socket


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("" . join(key))


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("" . join(orig_text))


def server_program():
    host = socket.gethostname()
    port = 4000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("\n")
        print('20BCS079 VIDIP GHOSH')
        print("\n")
        print("Encrypted message: ")
        print(data)
        print("\n")
        keyword = input(
            "Enter keyword set on client side to decrypt message: ")
        key = generateKey(data, keyword)
        print("Decrypted Text :", originalText(data, key))
        Decrypted = originalText(data, key)
        print("from connected user: " + str(Decrypted))

        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()
