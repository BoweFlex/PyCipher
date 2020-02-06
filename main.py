import sys
import inquirer

def main():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to Jonathan's Cipher and Encryption program!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    encrypt = input("Enter E to encrypt, D to decrypt, and Q to quit: ")
    print(encrypt)
    while encrypt.lower() != "e" or "d" or "q":
        encrypt = input("Please try again with a valid input (E, D, or Q): ")
        print(encrypt)

    if encrypt.lower() == "q":
        sys.exit()

    """encrypt = [
            inquirer.Confirm('encrypted',
                message="Would you like to encrypt?",
                default=True),
    ]
    encryption = inquirer.prompt(encrypt)
    print(encryption)
    encrypt = input("Would you like to encrypt? (Y/N): ")
    print(encrypt)
    if encrypt.lower() != "yes" or encrypt.lower() != "y":
        #print("I'm Here!")
        decrypt = input("Would you like to decrypt, then? (Y/N): ")
        print(decrypt)
        if decrypt.lower() != "yes" or decrypt.lower() != "y":
            print("Failure!")
            sys.exit()"""

    #change choices to be an object passed from folder with ciphers, this will work for now
    ciphers = [
            inquirer.List('options',
                message="What cipher would you like to use?",
                choices=['Caesar', 'Atbash'],
            ),
    ]
    chosenCipher = inquirer.prompt(ciphers)
    print(chosenCipher)

if __name__ == "__main__":
    main()
