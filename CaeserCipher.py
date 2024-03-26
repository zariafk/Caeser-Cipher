# CAESER CIPHER
import tkinter as tk

# Root window creation + details
window = tk.Tk()
window.geometry ('600x500')
window.title ('Caeser Cipher by Zaria')

# To clear window 
def clearWindow(window) :
    for widget in window.winfo_children() :
        widget.grid_forget()

# Adding a label to root window
label1 = tk.Label(window, text = 'Would you like to encrypt or decrypt text? ')
label1.grid(column = 0, row = 0)

#Functions for relevant buttons
def eClick() :
    clearWindow(window)
    eLabel = tk.Label(window, text = 'Encryption Mode')
    eLabel.grid(column = 0, row = 0, padx = 5, sticky = 'w')
    
    eInLabel = tk.Label(window, text = 'Please enter the text you would like to encrypt: ')
    eInLabel.grid(column = 0, row = 1, padx = 5, pady = 20, sticky = 'w')

    eInput = tk.Entry(window, width = 75)
    eInput.grid(column = 0, row = 2, padx = 70, pady = 20, sticky = 'sw')

    eExec = tk.Button(window, text = 'Encrypt', fg = 'red')
    eExec.grid(column = 0, row = 3, padx = 280, pady = 5, sticky = 'sw')

def dClick() :
    clearWindow(window)
    dLabel = tk.Label(window, text = 'Decryption Mode')
    dLabel.grid(column = 0, row = 0, padx = 5, sticky = 'w')

    dInLabel = tk.Label(window, text = 'Please enter the text you would like to decrypt: ')
    dInLabel.grid(column = 0, row = 1, padx = 5, pady = 20, sticky = 'w')

    dInput = tk.Entry(window, width = 75)
    dInput.grid(column = 0, row = 2, padx = 70, pady = 20, sticky = 'sw')

    dExec = tk.Button(window, text = 'Decrypt', fg = 'Green')
    dExec.grid(column = 0, row = 3, padx = 280, pady = 5, sticky = 'sw')

# Creating relevant buttons
eButton = tk.Button(window, text = 'Encrypt', bg = 'red', command = eClick)
eButton.grid(column = 1, row = 1, padx = 10, pady = 50)
dButton = tk.Button(window, text = 'Decrypt', bg = 'green', command = dClick)
dButton.grid(column = 2, row = 1, padx = 10, pady = 50)

# Execute tkinter
window.mainloop()

'''
def encrypt(text, key) :
    cipher = ''
    for letter in text :
        letter = letter.lower()
        i = alphabet.find(letter)
        if i == -1 :
            cipher += letter
        else :
            ci = i+3
            if ci > 25 :
                ci -= 26
            cipher += alphabet[ci]
    return cipher

def decrypt(cipher, key) :
    text = ''
    for letter in cipher :
        letter = letter.lower()
        ci = alphabet.find(letter)
        if ci == -1 :
            text += letter
        else :
            i = ci-3
            if i < 0 :
                i += 26
            text += alphabet[i]
    return text

def main() :
    global alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 3

    selection = input('Do you want to encrypt or decrypt?\n[Please enter e/d]\n')
    
    if selection != 'e' and selection != 'd' :
        print('Invalid input')
    else :
        text = input('Please enter text: ')
        if selection == 'e' :
            print(encrypt(text, key))
        elif selection == 'd' :
            print(decrypt(text, key)) 
    return

main()
'''