dictionary = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
              'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
              'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
              'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
              'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

# Function to encrypt the string according to the cipher provided


def encrypt(message):
    cipher = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # adds a cipher text corresponding to the plaintext from the dictionary
            cipher += dictionary[letter]
        else:
            # adds space
            cipher += ' '
    return cipher


def decrypt(message):
    decipher = ''
    i = 0
    while True:
        # condition to run decryption till the last set of the cipher text
        if (i < len(message)-4):
            substr = message[i:i+5]

            # checking for space as the first character of the substring
            if (substr[0] != ' '):
                decipher += list(dictionary.keys()
                                 )[list(dictionary.values()).index(substr)]
                i += 5  # moves to the next set of the cipher text
            else:
                decipher += ' '  # Adds space to it
                i += 1
        else:
            break
    return decipher


def main():
    message = input("Enter a plain text: ")
    result = encrypt(message.upper())
    print("Encryted text: ", result)

    message = input("Enter an encrypted text: ")
    result = decrypt(message.lower())
    print("Decrypted text: ", result)


# Executes the main function
if __name__ == '__main__':
    main()
