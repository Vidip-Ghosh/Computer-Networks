def toLowerCase(text):
    return text.lower()


def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText+i
    return newText


def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph


def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                newWord = text[0:i+1] + str('x') + text[i+1:]
                newWord = FillerLetter(newWord)
                break
            else:
                newWord = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                newWord = text[0:i+1] + str('x') + text[i+1:]
                newWord = FillerLetter(newWord)
                break
            else:
                newWord = text
    return newWord


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to generate 5X5 key square matrix


def generateKey(word, list1):
    keyLetters = []
    for i in word:
        if i not in keyLetters:
            keyLetters.append(i)

    compElements = []
    for i in keyLetters:
        if i not in compElements:
            compElements.append(i)

    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == element):
                return i, j


def encryptRowRule(mat, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = mat[e1r][0]
    else:
        char1 = mat[e1r][e1c+1]

    char2 = ''
    if e2c == 4:
        char2 = mat[e2r][0]
    else:
        char2 = mat[e2r][e2c+1]

    return char1, char2


def encryptColumnRule(mat, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = mat[0][e1c]
    else:
        char1 = mat[e1r+1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = mat[0][e1c]
    else:
        char2 = mat[e2r+1][e2c]

    return char1, char2


def encryptRectangleRule(mat, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = mat[e1r][e2c]

    char2 = ''
    char2 = mat[e2r][e1c]

    return char1, char2


def encryptPlayFairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        e1e1_x, e1e1_y = search(Matrix, plainList[i][0])
        e1e2_x, e1e2_y = search(Matrix, plainList[i][1])

        if e1e1_x == e1e2_x:
            c1, c2 = encryptRowRule(Matrix, e1e1_x, e1e1_y, e1e2_x, e1e2_y)

        elif e1e1_y == e1e2_y:
            c1, c2 = encryptColumnRule(Matrix, e1e1_x, e1e1_y, e1e2_x, e1e2_y)
        else:
            c1, c2 = encryptRectangleRule(
                Matrix, e1e1_x, e1e1_y, e1e2_x, e1e2_y)

        cipher = c1+c2
        CipherText.append(cipher)
    return CipherText


text_Plain = 'instruments'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1]+'z'

key = "Monarchy"
print("Key text:", key)
key = toLowerCase(key)
Matrix = generateKey(key, list1)

print("Plain Text:", text_Plain)
CipherList = encryptPlayFairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
    CipherText += i
print("CipherText:", CipherText)
