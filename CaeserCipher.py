# CAESER CIPHER

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