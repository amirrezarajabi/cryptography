import sys
import time
import os

class Shift_Cipher:

    def __init__(self, k):
        self.key = k
    
    def encrypt(self, plaintext):
        cipher = ["_"] * len(plaintext)
        k = str(self.key)
        print("Encrypt with k = " + k)
        print("#" * (len(plaintext) + 17))
        print("#" + " " *(len(plaintext) + 15) +"#")
        print("# PLAIN TEXT:  "+plaintext+" #")
        print("#" + " " *(len(plaintext) + 15) +"#")
        for i in range(len(plaintext)):
            cipher[i] = chr((ord(plaintext[i]) - 97 + self.key ) % 26 + 97)
            text_s = "".join(cipher)
            text_s = "# CIPHER TEXT: "+text_s + " #"
            print('\r{}'.format(text_s), end='')
            time.sleep(3/len(plaintext))
        print()
        print("#" + " " *(len(plaintext) + 15) +"#")
        print("#" * (len(plaintext) + 17))
        input()
        return text
    
    def decrypt(self, ciphertext):
        plain = ["_"] * len(ciphertext)
        k = str(self.key)
        print("Decrypt with k = " + k)
        print("#" * (len(ciphertext) + 17))
        print("#" + " " *(len(ciphertext) + 15) +"#")
        print("# CIPHER TEXT: "+ciphertext+" #")
        print("#" + " " *(len(ciphertext) + 15) +"#")
        for i in range(len(ciphertext)):
            plain[i] = chr((ord(ciphertext[i]) - 97 - self.key ) % 26 + 97)
            text = "".join(plain)
            text = "# PLAIN TEXT:  "+text + " #"
            print('\r{}'.format(text), end='')
            time.sleep(1.5/len(ciphertext))
        print()
        print("#" + " " *(len(ciphertext) + 15) +"#")
        print("#" * (len(ciphertext) + 17))
        input()
        return text
    
crypt = input("Decrypt or Encrypt (De/En): ")
text = input(crypt + "crypt: ")
k = int(input("Shift: "))
os.system('cls')
sc = Shift_Cipher(k)
if(crypt == "De"):
    sc.decrypt(text)
else:
    sc.encrypt(text)
