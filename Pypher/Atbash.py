

class Atbash:
    """Contains the dictionary for Atbash, and functions for decryption or encryption"""

    def __init__(self, ciphString=" "):
        self.ciphString = ciphString.strip();
        self.cipher = {
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

def atbashEncryption(self, string):
    tempLetter = 'a'
    for letter in string:
        tempLetter = self.cipher[letter]
        letter = tempLetter


def atbashDecryption(string):
    pass
