import hashlib
import time
import os
import random
import string
from colorama import Fore, Style, init
init(autoreset=True)
ADMIN_KEY_HASH = hashlib.sha256("my_secret_admin_key".encode()).hexdigest()
print("Admin hash loaded")


ascii_art = r"""

                  S%t%X@SXSSXXXXSXSS@XSXX%X                 
                  XX88@X8@@@@@@@@@8888888@@                 
                  @;;%XXSXSXSXSSSSXXS8@%ttS                 
                   ;S;88@88888888@88888t%S                  
                   @;tS8@888888@888@@8tS;8                  
                   X;tS8@@@@88@@@@@@8%X;t8                  
                   StSt88@@@88@@@8@@X8ttt@                  
                   S;tSt8@@@8@@@@@@@8%Xt%@                  
                   8;t%@8@@@@@@@@@8@8@%X;S                  
                   StS;t8@@@@@@@8@@@X8t%t8                  
                  X%8X@St@@@@@8@@@@@8%XSXS                  
               8888t;t;t@S%@%@8SX@SX%%tt;;888X              
         S@;;;t;;ttXt%Xt;tStXtt%SXtXtSt%%%tt;;t;tS@         
            88t%%S;t%t%%Xt;ttStX;t%tttSSXt%S;t@@8           
               @@;%XtSX;t%Stttt%Xt%SSS%X;S;88               
                   @SX;%S%t%@tXt%X%%XtSXX@                  
                                                
                   %.%8X:StX%.S 8t;%S%88X                   
                    @8S8S8S88SX8S@StXS%X                    
                  
"""
{Fore.RED}
print(ascii_art)
print("Welcome to Encryption Decryption Program")
role = input("are you admin or user(a/u): ").lower()
if role in ["a", "admin"]:
    role = "admin"
elif role in ["u", "user"]:
    role = "user"
else:
    print("Invalid role")
    exit()

all_charst=input("do you want to hash password or just encrypt it(h/e):   ") 
print("after hashing password you can't decrypt it back")  
if all_charst.lower()=='h':    
    
    password = input("Enter password to hash: ")
    hash_object = hashlib.sha256(password.encode())
    print(hash_object)
    hex_dig = hash_object.hexdigest()
    print(f" Hashed Password: {hex_dig}")
    import sys
    exit()
elif all_charst.lower()=='e':
 all_charst = string.ascii_letters + string.digits + string.punctuation + " "
all_charst = list(all_charst)
key =all_charst.copy()
random.shuffle(key)
print(f"all_charst:{all_charst}")
print()
print(f"key:{key}")
plain_text = input("Enter passwerd to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = all_charst.index(letter)
    cipher_text += key[index]
print(f"Ecrypted Message:{cipher_text}")
with open("data.txt", "w") as f:
    f.write("HASH="+hashlib.sha256(plain_text.encode()).hexdigest()+"\n")
loca = input("do you want decrypt it(y/n): ")
if loca.lower() == "y":
    if role == "admin":
        admin_key = input("Enter admin key: ")
        if hashlib.sha256(admin_key.encode()).hexdigest() != ADMIN_KEY_HASH:
            decipher_text = ""
            for letter in cipher_text:
                index = key.index(letter)
                decipher_text += all_charst[index]
            print(f"Decrypted Message:{decipher_text}")
        else:
            print("Wrong admin key")
    else:
        print("user mode .only hash is allowed")   
elif loca.lower() == 'n':
    print("Thank you for using our service")