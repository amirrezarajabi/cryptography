import sys
import time
import os
import clipboard

class Substitution_Cipher:

    def __init__(self, SPEED, LANGUAGE, k = None):
        self.key = k
        self.speed = SPEED
        self.language = LANGUAGE

    def encrypt(self, plaintext):
        cipher = ["_"] * len(plaintext)
        k = str(self.key)
        print("Encrypt with k = " + k)
        print("#" * (len(plaintext) + 17))
        print("#" + " " *(len(plaintext) + 15) +"#")
        print("# PLAIN TEXT:  "+plaintext+" #")
        print("#" + " " *(len(plaintext) + 15) +"#")
        for i in range(len(plaintext)):
            cipher[i] = self.language[self.convert(self.language.index(plaintext[i]), True)]
            text_s = "".join(cipher)
            text_s = "# CIPHER TEXT: "+text_s + " #"
            print('\r{}'.format(text_s), end='')
            time.sleep(self.speed/len(plaintext))
        print()
        print("#" + " " *(len(plaintext) + 15) +"#")
        print("#" * (len(plaintext) + 17))
        input()
        clipboard.copy("".join(cipher))
        return text_s
    
    def decrypt(self, ciphertext):
        plain = ["_"] * len(ciphertext)
        k = str(self.key)
        print("Decrypt with k = " + k)
        print("#" * (len(ciphertext) + 17))
        print("#" + " " *(len(ciphertext) + 15) +"#")
        print("# CIPHER TEXT: "+ciphertext+" #")
        print("#" + " " *(len(ciphertext) + 15) +"#")
        for i in range(len(ciphertext)):
            plain[i] = self.language[self.convert(self.language.index(ciphertext[i]), False)]
            text = "".join(plain)
            text = "# PLAIN TEXT:  "+text + " #"
            print('\r{}'.format(text), end='')
            time.sleep(self.speed/len(ciphertext))
        print()
        print("#" + " " *(len(ciphertext) + 15) +"#")
        print("#" * (len(ciphertext) + 17))
        input()
        clipboard.copy("".join(plain))
        return text

    def convert(self, i, crypt):
        if(crypt):
            return int(self.key[i])
        return int(self.key.index(str(i)))

    def do(self):
        crypt = input("Decrypt or Encrypt (De/En): ")
        text = input(crypt + "crypt: ")
        k = input("Substitution: ").split(" ")
        os.system('cls')
        self.key = k
        if(crypt == "De"):
            self.decrypt(text)
        else:
            self.encrypt(text)
