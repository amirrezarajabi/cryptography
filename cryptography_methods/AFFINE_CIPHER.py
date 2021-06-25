import sys
import time
import os
import clipboard

class Affine_Cipher:

    def __init__(self, SPEED, LANGUAGE, k=None):
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
            cipher[i] = self.language[(self.key[0] * self.language.index(plaintext[i]) + self.key[1] ) % len(self.language)]
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
            plain[i] = self.language[(self.arca() * (self.language.index(ciphertext[i]) - self.key[1])) % len(self.language)]
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

    def do(self):
        crypt = input("Decrypt or Encrypt (De/En): ")
        crypt = crypt.split(" ")
        crypt = "".join(crypt)
        text = input(crypt + "crypt: ")
        k = input("Key: ")
        k = k.split(" ")
        k[0] = int(k[0])
        k[1] = int(k[1])
        self.key = k
        os.system('cls')
        if(crypt == "De"):
            self.decrypt(text)
        else:
            self.encrypt(text)

    def arca(self):
        a = self.key[0]
        if(a == 1):
            return 1
        b = 2
        while((a * b) % len(self.language) != 1):
            b += 1
        return b
