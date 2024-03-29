# CAESER CIPHER ~by Zaria Farooq-Khan
import tkinter as tk

                                                                        # BASIC FUNCTIONS
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
# When encrypt/decrypt button is pressed at encryption/decryption window, respectively
def calcClick(text, ed) :
    result = eOrD(text, ed)
    resultLabel = tk.Label(window, text = result)
    resultLabel.grid(column = 0, row = 4, pady = 30)


# New rendering once encryption/decryption mode is selected (from initial window)
def modes(ed) :
    clearWindow(window)
    homeButton()

    # Only 'e' or 'd' will ever be passed in as ed, for encryption and decryption, respectively
    if ed == 'e' :
        labelText = 'Encryption'
        inpLabelText = 'encrypt'
        calcText = 'Encrypt'
        colr = 'red'
    else :
        labelText = 'Decryption'
        inpLabelText = 'decrypt'
        calcText = 'Decrypt'
        colr = 'green'

    label = tk.Label(window, text = labelText + 'Mode')
    label.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'w')

    inpLabel = tk.Label(window, text = 'Please enter the text you would like to ' + inpLabelText + ': ')
    inpLabel.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 'w')

    inp = tk.Entry(window, width = 75)
    inp.grid(column = 0, row = 2, padx = 70, pady = 20, sticky = 'sw')

    calc = tk.Button(window, text = calcText, fg = colr, command = lambda: calcClick(inp.get(), ed))
    calc.grid(column = 0, row = 3, padx = 280, pady = 5, sticky = 'sw')


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
    eButton = tk.Button(window, text = 'Encrypt', bg = 'red', command = lambda: modes('e'))
    eButton.grid(column = 1, row = 1, padx = 10, pady = 50)
    dButton = tk.Button(window, text = 'Decrypt', bg = 'green', command = lambda: modes('d'))
    dButton.grid(column = 2, row = 1, padx = 10, pady = 50)


                                                    # WINDOW RENDERING AND EXECUTION - FINAL
# Window rendering
window = tk.Tk()
window.geometry ('600x500')
window.title ('Caeser Cipher by Zaria')

# Execution
startRender()
window.mainloop()