from .caesar import caesar_decrypt

""" Initialized with the following:
    ciphString: User input string, to be encrypted, required
    cipher: Type of cipher to be used, defaults to caesar
    shift: Allows for full functionality of caesar, usually not input
    mod: Number of letters in alphabet, usually not input"""
class Decrypt:

    def __init__(self, ciphString=" ", cipher = "caesar", shift=3, mod= 26):
        self.ciphString = ciphString
        self.cipher = cipher
        self.shift = shift
        self.mod = mod

        self.ciphers = {
                "caesar": caesar_decrypt(ciphString, shift, mod)
        }

    def get_decryption(self):
        word = self.ciphers.get(self.cipher)
        return word
