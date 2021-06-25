from cryptography_methods.SHIFT_CIPHER import Shift_Cipher
from cryptography_methods.AFFINE_CIPHER import Affine_Cipher
from cryptography_methods.SUBSTITUTION_CIPHER import Substitution_Cipher
from cryptography_methods.VIGENERE_CIPHER import Vigenere_Cipher
import os

LANGUAGE = "abcdefghijklmnopqrstuvwxyz"
SPEED = 1.5

def print_logo():
    print("""
        ___                 _                                       ____       ______   
       / _ \               (_) __    __ ______    ______           |  _ \     |__  __|  
      / /_\ \    _ __ ___  __ /  /  /  /       \ /_____ /          | | \ \       | |    
     /_______\  | '_ ` _ \/  |  |  |  | ________\    / /    __ _   | |_/ /       | |  
    /         \ | | | | | |  |  |  |  | \      __   / /    / _` \  |____/ __     | |    
   /	       || | | | | |  |  |  |  |\ \____/ /  / /____/ (_| |  |    \ | |____| |    
  /            ||_| |_| |_|__|__|  |__| \______/  /______/\__,__|  |     \|________|    
    """)

def menu():
    os.system("cls")
    print_logo()
    print("\n[1] Do cryptography")
    print("[2] Solve a cryptography")
    print("[3] Settings")
    print("[4] Exit")
    while(1):
        mode = int(input(">>> "))
        if(mode == 1):
            cryptosystem()
            break
        elif(mode == 2):
            exit()
            break
        elif(mode == 3):
            settings()
            break
        elif(mode == 4):
            exit()
            break
        else:
            print("invalid choose")

def cryptosystem():
    os.system("cls")
    print_logo()
    print("\n[1] Shift cipher")
    print("[2] Substitution cipher")
    print("[3] Affine cipher")
    print("[4] Vigenere cipher")
    print("[5] Menu")
    print("[6] exit")
    while(1):
        mode = int(input(">>> "))
        if(mode == 1):
            sc = Shift_Cipher(SPEED, LANGUAGE)
            sc.do()
            cryptosystem()
        elif(mode == 2):
            sc = Substitution_Cipher(SPEED, LANGUAGE)
            sc.do()
            cryptosystem()
        elif(mode == 3):
            ac = Affine_Cipher(SPEED, LANGUAGE)
            ac.do()
            cryptosystem()
        elif(mode == 4):
            vc = Vigenere_Cipher(SPEED, LANGUAGE)
            vc.do()
            cryptosystem()
        elif(mode == 5):
            menu()
        elif(mode == 6):
            exit()
            break
        else:
            print("invalid choose")

def settings():
    os.system("cls")
    print_logo()
    print("\n[1] Delay")
    print("[2] Language")
    print("[3] Menu")
    print("[4] exit")
    while(1):
        mode = int(input(">>> "))
        if(mode == 1):
            SPEED = float(input("Delay (default delay is 1.5): "))
            settings()
            break
        elif(mode == 2):
            languages()
            break
        elif(mode == 3):
            menu()
        elif(mode == 4):
            exit()
            break
        else:
            print("invalid choose")

def languages():
    os.system("cls")
    print_logo()
    print("\n[1] Add to default language(" + LANGUAGE + ")")
    print("[2] Set language")
    print("[4] Settings")
    print("[4] Menu")
    print("[5] exit")
    while(1):
        mode = int(input(">>> "))
        if(mode == 1):
            LANGUAGE += input("Characters to add "+ LANGUAGE +" without space: ")
            settings()
            break
        elif(mode == 2):
            LANGUAGE = input("Set Language: ")
            languages()
            break
        elif(mode == 4):
            menu()
            break
        elif(mode == 3):
            settings()
            break
        elif(mode == 5):
            exit()
            break
        else:
            print("invalid choose")
menu()
