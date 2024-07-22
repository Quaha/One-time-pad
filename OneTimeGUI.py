from tkinter import *
from tkinter import messagebox

import VigenereCipher
from VigenereCipher import LETTERS

import sys
import secrets
import time

PROGRAM_NAME = "One-time pad"
VERSION = "V1.02 from 23.07.21"

MAIN_BUTTON_WIDTH = 25

FIRST_BUTTON_FONT = 'Comic Sans MS'
SECOND_BUTTON_FONT = 'Lucida Console'


def main():
    global window

    # Creating a window
    window = Tk()
    window.title(PROGRAM_NAME)
    window['bg'] = '#bbbbbb'
    window.geometry('720x480')
    window.resizable(width=False, height=False)
    window.iconbitmap('notepad.ico')

    canvas = Canvas(window, width=720, height=480)
    canvas.pack()

    Label(window, text=PROGRAM_NAME, bg='grey94', font=(SECOND_BUTTON_FONT, 20)).place(relx=0.365, rely=0.025)
    Label(window, text=VERSION, bg='grey94', font=(SECOND_BUTTON_FONT, 8)).place(x=570, y=465)

    mainMenu()  # Opening the menu

    window.mainloop()


def encryptMenu():
    def btn_encrypt_command():
        if len(message.get()) == 0:
            messagebox.showinfo('Encryption', 'Encryption error: You didn\'t enter the message.')
        else:
            key = ''
            for i in range(len(message.get())):
                key += secrets.choice(LETTERS)
            translated = VigenereCipher.encryptMessage(key, message.get())
            if len(key) > 256:
                messagebox.showinfo('Encryption',
                                    'Your message and the encryption key were recorded in a .txt file in the encryption program directory.')
            else:
                messagebox.showinfo('Encryption',
                                    'For convenience, your encrypted message and key will be written to a .txt file in the encryption program directory.\n' +
                                    'Your message: ' + str(translated) + '\n' + 'Your key: ' + str(
                                        key))

            file_name = str(time.ctime()).replace(':', '.') + '.txt'
            file_obj = open('Encrypted message from the ' + file_name, 'w')
            file_obj.write('Your message: ' + str(translated) + '\n')
            file_obj.write('Your key: ' + str(key))
            file_obj.close()

    encrypt_frame = Frame(window, bg='grey85')
    encrypt_frame.place(rely=0.12, relwidth=1, relheight=0.76)

    # Buttons
    Button(encrypt_frame, text='Exit', bg='grey80', font=(SECOND_BUTTON_FONT, 10), command=sys.exit).place(x=660, y=330)
    Button(encrypt_frame, text='Back', bg='grey80', font=(SECOND_BUTTON_FONT, 10), command=mainMenu).place(x=5, y=330)

    Label(encrypt_frame, text='Encryption', bg='grey85', font=(FIRST_BUTTON_FONT, 18)).pack()

    message = StringVar()
    Entry(encrypt_frame, textvariable=message, bg='grey94', justify='center', width=50,
          font=(FIRST_BUTTON_FONT, 8)).place(relx=0.3, y=130)
    Label(encrypt_frame, text='Message:', bg='grey85', font=(FIRST_BUTTON_FONT, 13)).place(x=75, y=120)
    Button(encrypt_frame, text='Encrypt a message \nwith a random key', bg='grey80', font=(SECOND_BUTTON_FONT, 12),
           command=btn_encrypt_command).place(relx=0.3, y=170)

    window.update()


def decryptMenu():
    def btn_decrypt_command():
        if len(message.get()) == 0:
            messagebox.showinfo('Decryption', 'Decryption error: You did not enter the message.')
        elif len(key.get()) == 0:
            messagebox.showinfo('Decryption', 'Decryption error: You did not enter the key.')
        else:
            translated = VigenereCipher.decryptMessage(key.get(), message.get())
            if savefile.get():
                file_name = str(time.ctime()).replace(':', '.') + '.txt'
                file_obj = open('Decrypted message from the ' + file_name, 'w')
                file_obj.write('Your message: ' + str(translated))
                file_obj.close()
                if len(translated) <= 256:
                    messagebox.showinfo('Decryption',
                                        'Your message: ' + translated + '\nA copy of the message is located in the .txt file in the program directory.')
                else:
                    messagebox.showinfo('Decryption',
                                        'Your message is saved in a .txt file in the program directory.')
            elif len(translated) <= 256:
                messagebox.showinfo('Decryption', 'Your message: ' + translated)
            else:
                messagebox.showinfo('Decryption',
                                    'Your message is too long, so it will be forcibly saved to a .txt file in the program directory.')
                file_name = str(time.ctime()).replace(':', '.') + '.txt'
                file_obj = open('Decrypted message from the ' + file_name, 'w')
                file_obj.write('Your message: ' + str(translated))
                file_obj.close()

    decrypt_frame = Frame(window, bg='grey85')
    decrypt_frame.place(rely=0.12, relwidth=1, relheight=0.76)

    # Buttons
    Button(decrypt_frame, text='Exit', bg='grey80', font=(SECOND_BUTTON_FONT, 10), command=sys.exit).place(x=660, y=330)
    Button(decrypt_frame, text='Back', bg='grey80', font=(SECOND_BUTTON_FONT, 10), command=mainMenu).place(x=5,
                                                                                                           y=330)

    Label(decrypt_frame, text='Decoding', bg='grey85', font=(FIRST_BUTTON_FONT, 18)).pack()

    Label(decrypt_frame, text='Message:', bg='grey85', font=(FIRST_BUTTON_FONT, 13)).place(x=75, y=75)
    Label(decrypt_frame, text='Key:', bg='grey85', font=(FIRST_BUTTON_FONT, 13)).place(x=75, y=125)
    message = StringVar()
    key = StringVar()
    Entry(decrypt_frame, textvariable=message, bg='grey94', justify='center', width=50,
          font=(FIRST_BUTTON_FONT, 8)).place(relx=0.3, y=85)
    Entry(decrypt_frame, textvariable=key, bg='grey94', justify='center', width=50,
          font=(FIRST_BUTTON_FONT, 8)).place(relx=0.3, y=135)
    Button(decrypt_frame, text='Decrypt the message', bg='grey80', font=(SECOND_BUTTON_FONT, 12),
           command=btn_decrypt_command).place(relx=0.1, y=185)
    savefile = BooleanVar()
    Checkbutton(decrypt_frame, text='Save the message to a .txt file', variable=savefile, bg='grey85').place(x=365,
                                                                                                             y=187)
    window.update()


def mainMenu():
    def info():
        with open('info.txt', 'r', encoding="UTF-8") as txtObj:
            my_text = txtObj.read()
        messagebox.showinfo('Information', my_text)

    menu_frame = Frame(window, bg='grey85')
    menu_frame.place(rely=0.12, relwidth=1, relheight=0.76)

    Button(menu_frame, text='Encrypt the message', bg='grey80', font=(FIRST_BUTTON_FONT, 15),
           command=encryptMenu, width=MAIN_BUTTON_WIDTH).pack(pady=15)
    Button(menu_frame, text='Decrypt the message', bg='grey80', font=(FIRST_BUTTON_FONT, 15),
           command=decryptMenu, width=MAIN_BUTTON_WIDTH).pack(pady=15)
    Button(menu_frame, text='Information', bg='grey80', font=(FIRST_BUTTON_FONT, 15),
           command=info, width=MAIN_BUTTON_WIDTH).pack(pady=15)
    Button(menu_frame, text='Exit', bg='grey80', font=(FIRST_BUTTON_FONT, 15),
           command=sys.exit, width=MAIN_BUTTON_WIDTH).pack(pady=15)

    window.update()


if __name__ == '__main__':
    main()
