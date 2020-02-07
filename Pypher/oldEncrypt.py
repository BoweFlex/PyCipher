

""" I was going to use this to do encryption via substitution, but have since replaced it with a formula based cipher system"""
class Ciphers:
    """Contains the dictionary for no-key ciphers, and functions for decryption or encryption"""
    """Use an object for a list of ciphers to interact with main.py and call different cipher objects with the different formulas inside functions that can be called by list obj"""
    def __init__(self, ciphString=" "):
        self.ciphString = ciphString.strip();
        self.ciphers = {
                Atbash = {
                    'a': 'z',
                    'b': 'y',
                    'c': 'x',
                    'd': 'w',
                    'e': 'v',
                    'f': 'u',
                    'g': 't',
                    'h': 's',
                    'i': 'r',
                    'j': 'q',
                    'k': 'p',
                    'l': 'o',
                    'm': 'n',
                    'n': 'm',
                    'o': 'l',
                    'p': 'k',
                    'q': 'j',
                    'r': 'i',
                    's': 'h',
                    't': 'g',
                    'u': 'f',
                    'v': 'e',
                    'w': 'd',
                    'x': 'c',
                    'y': 'b',
                    'z': 'a'
                }
                Caesar = {
                    'a': 'x',
                    'b': 'y',
                    'c': 'z',
                    'd': 'a',
                    'e': 'b',
                    'f': 'c',
                    'g': 'd',
                    'h': 'e',
                    'i': 'f',
                    'j': 'g',
                    'k': 'h',
                    'l': 'i',
                    'm': 'j',
                    'n': 'k',
                    'o': 'l',
                    'p': 'm',
                    'q': 'n',
                    'r': 'o',
                    's': 'p',
                    't': 'q',
                    'u': 'r',
                    'v': 's',
                    'w': 't',
                    'x': 'u',
                    'y': 'v',
                    'z': 'w'
                }

def caesarEncryption(self, string):
    tempLetter = 'a'
    for letter in string:
        tempLetter = self.cipher.get(letter, 'a')
        letter = tempLetter


def caesarDecryption(string):
    pass
