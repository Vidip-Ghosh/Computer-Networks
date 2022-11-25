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


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):

        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("" . join(cipher_text))


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("" . join(orig_text))


def client_program():
    host = socket.gethostname()
    port = 4000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    keyword = input("Enter keyword ")
    key = generateKey(message, keyword)
    cipher_text = cipherText(message, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))

    while message.lower().strip() != 'bye':
        client_socket.send(cipher_text.encode())
        data = client_socket.recv(1024).decode()
        print("\n")
        print('20BCS079 VIDIP GHOSH')
        print('Received from server: ' + data)
        print('characters received from server: ')
        message = input(" -> ")

        keyword = input("Enter keyword ")
        key = generateKey(message, keyword)
        cipher_text = cipherText(message, key)
        print("Ciphertext :", cipher_text)
        print("Original/Decrypted Text :", originalText(cipher_text, key))
    client_socket.close()


if __name__ == '__main__':
    client_program()
