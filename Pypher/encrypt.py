from .caesar import caesar_encrypt
from .atbash import atbash_encrypt

""" Initialized with the following:
    ciphString: User input string, to be encrypted, required
    cipher: Type of cipher to be used, Defaults to caesar
    shift: Allows for full functionality of caesar, usually not input
    mod: Number of letters in alphabet, usually not input"""
class Encrypt:
    """Contains the dictionary for no-key ciphers, and functions for decryption or encryption"""
    """Use an object for a list of ciphers to interact with main.py and call different cipher objects with the different formulas inside functions that can be called by list obj"""
    def __init__(self, ciphString=" ", cipher = "caesar", shift=3, mod=26):
        self.ciphString = ciphString
        self.cipher = cipher
        self.shift = shift
        self.mod = mod

        self.ciphers = {
                "caesar": caesar_encrypt(ciphString, shift, mod),
                "atbash": atbash_encrypt(ciphString, shift, mod)
        }
    def get_encryption(self):
        return self.ciphers.get(cipher)
