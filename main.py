from SHIFT_CIPHER import Shift_Cipher
from SUBSTITUTION_CIPHER import Substitution_Cipher
import os

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
    print("[3] Exit")
    while(1):
        mode = int(input(">>> "))
        if(mode == 1):
            cryptosystem()
            break
        elif(mode == 2):
            exit()
            break
        elif(mode == 3):
            exit()
            break
        else:
            print("invalid choose")

def cryptosystem():
    os.system("cls")
    print_logo()
    print("\n[1] Shift cipher")
    print("[2] Substitution cipher")
    print("[3] Menu")
    print("[4] exit")
    while(1):
        mode = int(input(">>> "))
        if(mode == 1):
            sc = Shift_Cipher()
            sc.do()
            cryptosystem()
        elif(mode == 2):
            sc = Substitution_Cipher()
            sc.do()
            cryptosystem()
        elif(mode == 3):
            menu()
        elif(mode == 4):
            exit()
            break
        else:
            print("invalid choose")
menu()