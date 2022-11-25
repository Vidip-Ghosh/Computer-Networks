from cgitb import text
from unittest import result


def encrypt(text, k):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypting the uppercase letter
        if (char.isupper()):
            result += chr((ord(char) + k-65) % 26 + 65)
        # Encrypting the lowercase letter
        else:
            result += chr((ord(char) + k-97) % 26 + 97)
    return result


def decrypt(cipherText, k):
    result = ""
    for i in range(len(cipherText)):
        char = cipherText[i]
        if (char.isupper()):
            result += chr((ord(char)-k-65) % 26 + 65)
        else:
            result += chr((ord(char)-k-97) % 26 + 97)
    return result


text = "COMPUTER NETWORKING LAB"
s = 4
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))

cipherText = "GSQTYXIVrRIXASVOMRKrPEF"
k = 4
print("Plain Text: " + decrypt(cipherText, k))
