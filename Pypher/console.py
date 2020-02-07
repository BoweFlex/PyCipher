import  inquirer

class ConsoleInput():

    @staticmethod
    def get_cipher():
        #Fill with inquirer list of ciphers
        ciphers = [
                inquirer.List('options',
                    message="What cipher would you like to use?",
                    choices=['Caesar', 'Quit'],
                    ),
        ]
        return inquirer.prompt(ciphers)
   
    @staticmethod
    def get_cryption():
        #Fill with inquirer choice for encryption or decryption
        cryption = [
                inquirer.List('options',
                    message="Would you like to encrypt or decrypt?",
                    choices=['Encrypt', 'Decrypt', 'Quit'],
                    ),
        ]
        return inquirer.prompt(cryption)
    
    @staticmethod
    def get_word(encryptionOption="encrypt"):
        #Fill with input to receive word to encrypt/decrypt
        if(encryptionOption == "encrypt"):
            word = input("Please enter what you'd like to encrypt: ")
        else:
            word = input("Please enter what you'd like to decrypt: ")
        return word

