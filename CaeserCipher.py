# CAESER CIPHER
import tkinter as tk

# Root/initial window creation + details
window = tk.Tk()
window.geometry ('600x500')
window.title ('Caeser Cipher by Zaria')

# To clear window 
def clearWindow(window) :
    for widget in window.winfo_children() :
        widget.grid_forget()

# Adding a label to root window
label1 = tk.Label(window, text = 'Would you like to encrypt or decrypt text? ')
label1.grid(column = 0, row = 0, padx = 5, pady = 5)

# Functions for relevant buttons
# Global alphabet variable for functions
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Function to encrypt plaintext
def encrypt(plain) :
    key = 3 # typical caeser cipher key
    cipher = ''
    for letter in plain :
        letter = letter.lower()
        i = alphabet.find(letter)
        if i == -1 :
            cipher += letter
        else : # accounts for x,y,z where there are <3 letters after them
            ci = i+key
            if ci > 25 :
                ci -= 26
            cipher += alphabet[ci]
    return cipher

# Function to decrypt ciphertext
def decrypt(cipher) :
    key = 3 # typical caeser cipher key
    plain = ''
    for letter in cipher :
        letter = letter.lower()
        ci = alphabet.find(letter)
        if ci == -1 :
            plain += letter
        else : # accoutns for a,b,c where there are <3 letters before them
            i = ci-key
            if i < 0 :
                i += 26
            plain += alphabet[i]
    return plain

# When encrypt button is pressed at encryption window
def eExecClick(plain) :
    cipher = encrypt(plain)
    cipherLabel = tk.Label(window, text = cipher)
    cipherLabel.grid(column = 0, row = 4, pady = 30)

# When decrypt button is pressed at decryption window
def dExecClick(cipher) :
    plain = decrypt(cipher)
    plainLabel = tk.Label(window, text = plain)
    plainLabel.grid(column = 0, row = 4, pady = 30)

# When the encryption button is pressed from initial window
def eClick() :
    clearWindow(window)
    eLabel = tk.Label(window, text = 'Encryption Mode')
    eLabel.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'w')
    
    eInLabel = tk.Label(window, text = 'Please enter the text you would like to encrypt: ')
    eInLabel.grid(column = 0, row = 1, padx = 5, pady = 20, sticky = 'w')

    eInput = tk.Entry(window, width = 75)
    eInput.grid(column = 0, row = 2, padx = 70, pady = 20, sticky = 'sw')

    eExec = tk.Button(window, text = 'Encrypt', fg = 'red', command = lambda: eExecClick(eInput.get()))
    eExec.grid(column = 0, row = 3, padx = 280, pady = 5, sticky = 'sw')

# When decryption button is pressed from initial window
def dClick() :
    clearWindow(window)
    dLabel = tk.Label(window, text = 'Decryption Mode')
    dLabel.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'w')

    dInLabel = tk.Label(window, text = 'Please enter the text you would like to decrypt: ')
    dInLabel.grid(column = 0, row = 1, padx = 5, pady = 20, sticky = 'w')

    dInput = tk.Entry(window, width = 75)
    dInput.grid(column = 0, row = 2, padx = 70, pady = 20, sticky = 'sw')

    dExec = tk.Button(window, text = 'Decrypt', fg = 'Green', command = lambda: dExecClick(dInput.get()))
    dExec.grid(column = 0, row = 3, padx = 280, pady = 5, sticky = 'sw')

# Creating buttons for initial window
eButton = tk.Button(window, text = 'Encrypt', bg = 'red', command = eClick)
eButton.grid(column = 1, row = 1, padx = 10, pady = 50)
dButton = tk.Button(window, text = 'Decrypt', bg = 'green', command = dClick)
dButton.grid(column = 2, row = 1, padx = 10, pady = 50)

# Execute tkinter
window.mainloop()