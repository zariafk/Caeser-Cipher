# CAESER CIPHER
import tkinter as tk

# Initial functions
# To clear window 
def clearWindow(window) :
    for widget in window.winfo_children() :
        widget.grid_forget()


# Home button to go to intila startup screen
def homeButton() :
    hButton = tk.Button(window, text = 'Home', bg = 'black', fg = 'white', command = lambda: startRender())
    hButton.grid(column = 0, row = 0, padx = 20, pady = 5, sticky = 'e')



                                                                    # ENCRYPT/DECRYPT FUNCTION
# Encypting/Decrypting function
def eOrD(text, ed) :
    key = 3
    result = ''
    for letter in text :
        letter = letter.lower()
        original = alphabet.find(letter)
        if original == -1 :
            result += letter
        else :
            if ed == 'e' :
                new = original + key
                if new > 25 :
                    new -= 26
                result += alphabet[new]
            elif ed == 'd' :
                new = original - key
                if new < 0 :
                    new += 26
                result += alphabet[new]
    return result



                                                                        # BUTTON FUNCTIONS
# When encrypt button is pressed at encryption window   
def eExecClick(plain) :
    cipher = eOrD(plain, 'e')
    cipherLabel = tk.Label(window, text = cipher)
    cipherLabel.grid(column = 0, row = 4, pady = 30)


# When decrypt button is pressed at decryption window
def dExecClick(cipher) :
    plain = eOrD(cipher, 'd')
    plainLabel = tk.Label(window, text = plain)
    plainLabel.grid(column = 0, row = 4, pady = 30)


# When the encryption button is pressed from initial window
def eClick() :
    clearWindow(window)
    homeButton()

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
    homeButton()

    dLabel = tk.Label(window, text = 'Decryption Mode')
    dLabel.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'w')

    dInLabel = tk.Label(window, text = 'Please enter the text you would like to decrypt: ')
    dInLabel.grid(column = 0, row = 1, padx = 5, pady = 20, sticky = 'w')

    dInput = tk.Entry(window, width = 75)
    dInput.grid(column = 0, row = 2, padx = 70, pady = 20, sticky = 'sw')

    dExec = tk.Button(window, text = 'Decrypt', fg = 'Green', command = lambda: dExecClick(dInput.get()))
    dExec.grid(column = 0, row = 3, padx = 280, pady = 5, sticky = 'sw')



                                                                                # START WINDOW
# Initial window                                                   
def startRender() :
    # Global alphabet variable used in multiple functions
    global alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Root/initial window creation + details
    # Clear window
    clearWindow(window)
    
    # Adding a label to root window
    label1 = tk.Label(window, text = 'Would you like to encrypt or decrypt text? ')
    label1.grid(column = 0, row = 0, padx = 5, pady = 5)

    # Creating buttons for initial window
    eButton = tk.Button(window, text = 'Encrypt', bg = 'red', command = eClick)
    eButton.grid(column = 1, row = 1, padx = 10, pady = 50)
    dButton = tk.Button(window, text = 'Decrypt', bg = 'green', command = dClick)
    dButton.grid(column = 2, row = 1, padx = 10, pady = 50)



# Execute
window = tk.Tk()
window.geometry ('600x500')
window.title ('Caeser Cipher by Zaria')

startRender()
window.mainloop()