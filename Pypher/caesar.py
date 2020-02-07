""" Encryption for Caesar:
    ------Arguments------
    word: User input, required
    shift: Can be input, default of 3
    mod: Number of letters in alphabet, default 26
    ---Expected Output---
    Input1:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Output1: XYZABCDEFGHIJKLMNOPQRSTUVW
    Input2:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
    Output2: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"""
def caesar_encrypt(word, shift=3, mod=26):
    output = ""
    if (type(word) != str):
        return "Input must be a string"
    else:    
        for letter in word:
            if (letter.isupper()):
                ascChar = ord(letter)
                newChar = chr((ascChar - shift - 65) % mod + 65)
                output += newChar
            elif (letter.islower()):
                ascChar = ord(letter)
                newChar = chr((ascChar - shift - 97) % mod + 97)
                output += newChar
            else:
                output += letter
        return output

""" Decryption for Caesar:
    ------Arguments------
    Word: User input, required
    Shift: Can be input, default of 3
    Mod: Number of letters in alphabet, default 26
    ---Expected Output---
    Input1:  XYZABCDEFGHIJKLMNOPQRSTUVW
    Output1: ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
def caesar_decrypt(word, shift=3, mod=26):
    output = ""
    if (type(word) != str):
        return "Input must be a string"
    else:    
        for letter in word:
            if (letter.isupper()):
                ascChar = ord(letter)
                newChar = chr((ascChar + shift - 65) % mod + 65)
                output += newChar
            elif (letter.islower()):
                ascChar = ord(letter)
                newChar = chr((ascChar + shift - 97) % mod + 97)
                output += newChar
            else:
                output += letter
        return output
