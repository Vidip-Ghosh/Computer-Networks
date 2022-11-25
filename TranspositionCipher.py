import math
key = 'HACK'

# Encryption


def encryptMessage(msg):
    cipher = ""
    keyIndex = 0
    msgLen = float(len(msg))
    msgLst = list(msg)
    keyLst = sorted(list(key))

    col = len(key)  # No of columns
    row = int(math.ceil(msgLen/col))  # No of rows

    # Adding the character '_' in empty cell of the matrix
    fillNull = int((row*col) - msgLen)
    msgLst.append('_' * fillNull)

    # Create a matrix and insert the message and '_' character row wise
    matrix = [msgLst[i: i+col]
              for i in range(0, len(msgLst), col)]

    for _ in range(col):
        curr_idx = key.index(keyLst[keyIndex])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        keyIndex += 1
    return cipher


def decryptMessage(cipherText):
    msg = ""
    keyIndex = 0
    msgIndex = 0
    msgLen = float(len(cipherText))
    msgLst = list(cipherText)

    col = len(key)
    row = int(math.ceil(msgLen/col))

    keyList = sorted(list(key))

    # Creating an empty array to store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        currIdx = key.index(keyList[keyIndex])
        for j in range(row):
            dec_cipher[j][currIdx] = msgLst[msgIndex]
            msgIndex += 1
        keyIndex += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeatingg words")
    nullCount = msg.count('_')

    if nullCount > 0:
        return msg[:-nullCount]
    return msg


if __name__ == '__main__':
    msg = "Computer"

    cipher = encryptMessage(msg)
    print("Encrypted Message: {}".
          format(cipher))
    print("Decryped Message: {}".
          format(decryptMessage(cipher)))
