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
    if (type(word) == char):
        ascChar = ord(word)
        output = chr((ascChar + shift) % mod)
        return output
    elif (type(word) == str):
        for letter in word:
            ascChar = ord(letter)
            newChar = chr((ascChar + shift) % mod)
            output += ascChar
        return output
    else:
        return "Input must be either a string or character"

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
    if (type(word) == char):
        ascChar = ord(word)
        output = chr((ascChar - shift) % mod)
        return output
    elif (type(word) == str):
        for letter in word:
            ascChar = ord(letter)
            newChar = chr((ascChar - shift) % mod)
            output += ascChar
        return output
    else:
        return "Input must be either a string or character"
