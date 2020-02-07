import sys
from Pypher import ConsoleInput, Encrypt, Decrypt

def main():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to Jonathan's Cipher and Encryption program!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    
    print("++++++++++Choose quit at any time to exit.++++++++++\n")
    cipherDict = ConsoleInput.get_cipher()
    cipher = cipherDict.get("options").lower()

    if (cipher == "quit"):
        sys.exit()
    
    encryptionDict = ConsoleInput.get_cryption()
    encryption = encryptionDict.get("options").lower()

    if (encryption == "quit"):
        sys.exit()
    
    wordOption = ConsoleInput.get_word(encryption)
    if (encryption == "encrypt"):
        work = Encrypt(wordOption, cipher)
        print("Your encrypted message is: " + str(work.get_encryption()))
    elif (encryption == "decrypt"):
        work = Decrypt(wordOption, cipher)
        print("Your decrypted message is: " + str(work.get_decryption()))

if __name__ == "__main__":
    main()
