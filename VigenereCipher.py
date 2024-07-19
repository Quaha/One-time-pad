import pyperclip
import sys


def main():
    message = input('Enter message: ')
    key = input('Enter key: ')
    if len(key) > len(message):
        sys.exit('Error: Invalid key.')
    mode = int(input('Enter mode (0 - encrypt, 1 - decrypt): '))

    if mode == 0:
        translated = encryptMessage(key, message)
    elif mode == 1:
        translated = decryptMessage(key, message)
    else:
        sys.exit('Error: Invalid mode.')

    print('Your message:', translated)
    pyperclip.copy(translated)


def encryptMessage(key, message):
    return translatedMessage(key, message, 0)


def decryptMessage(key, message):
    return translatedMessage(key, message, 1)


def translatedMessage(key, message, mode):
    translated = []

    key_index = 0

    for symbol in message:
        number = LETTERS.find(symbol)
        if number != -1:
            if mode == 0:
                number += LETTERS.find(key[key_index])
            else:
                number -= LETTERS.find(key[key_index])

            number %= len(LETTERS)

            translated.append(LETTERS[number])

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)
    return ''.join(translated)


with open("alpabet.txt", 'r', encoding="UTF-8") as txtObj:
    LETTERS = txtObj.read()

if __name__ == '__main__':
    main()
