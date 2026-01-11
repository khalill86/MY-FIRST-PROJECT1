import hashlib
import json
import time
import os
import random
import string
def encrypt_text(text):
    characters = list(string.ascii_letters + string.digits + string.punctuation + " \n\t")
    key = characters.copy()
    random.shuffle(key)

    encrypted = ""
    for ch in text:
        encrypted += key[characters.index(ch)]

    return encrypted, key, characters


def decrypt_text(encrypted, key, characters):
    decrypted = ""
    for ch in encrypted:
        decrypted += characters[key.index(ch)]
    return decrypted

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
                  X%8X@St@@@@@8@@@@@8%SSSS                 
               8888t;t;t@S%@%@8SX@SX%%tt;;888X              
         S@;;;t;;ttXt%Xt;tStXtt%SXtXtSt%%%tt;;t;tS@         
            88t%%S;t%t%%Xt;ttStX;t%tttSSXt%S;t@@8           
               @@;%XtSX;t%Stttt%Xt%SSS%X;S;88               
                   @SX;%S%t%@tXt%X%%XtSXX@                  
                        00O|      |O00       
                   %.%8X:StX%.S 8t;%S%88X                   
                    @8S8S8S88SX8S@StXS%X                    
                  
"""
{Fore.RED}
print(ascii_art)
print("Welcome to Encryption Decryption Program")
all_charst=input("do you want to hash password or just encrypt it(h/e):   ") 
print("after hashing password you can't decrypt it back")  
if all_charst.lower()=='h':    
    
    password = input("Enter password to hash: ")
    hash_object = hashlib.sha256(password.encode())
    print(hash_object)
    hex_dig = hash_object.hexdigest()
    print(f" Hashed Password: {hex_dig}")
    import sys
    init(autoreset=True)
DATA_FILE = "channels.json"
def load_channels():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_channels(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def encrypt_password(password):
    characters = list(string.ascii_letters + string.digits + string.punctuation + " ")
    key = characters.copy()
    random.shuffle(key)

    encrypted = ""
    for ch in password:
        encrypted += key[characters.index(ch)]

    return encrypted, key, characters

def decrypt_password(encrypted, key, characters):
    decrypted = ""
    for ch in encrypted:
        decrypted += characters[key.index(ch)]
    return decrypted    
channels = load_channels()

role = input("Do you want to login as user or admin? (u/a): ").lower()

if role in ("a", "admin"):
    role = "admin"
elif role in ("u", "user"):
    role = "user"
else:
    print("Invalid choice")
    exit()

# ADMIN SECTION|||||||||||||||||||||||||||||||||||||||||||||||||||||||ßßßßßßßßßßßßßßßßßß

if role == "admin":
    print("\n[Admin mode]")

    filename = input("Enter the file name: ")
    if not os.path.exists(filename):
        print("File not found")
        exit()

    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()

    channel_id = input("Enter channel number: ")
    password = input("Set a password for this channel: ")

    pwd_hash = hash_password(password)


    encrypted_content, key, chars = encrypt_text(file_content)

  
    channels[channel_id] = {
        "hash": pwd_hash,
        "encrypted_content": encrypted_content,
        "key": key,
        "chars": chars,
        "filename": filename
    }

    save_channels(channels)


    with open(filename, "w", encoding="utf-8") as f:
        f.write(encrypted_content)

    print("\nFile encrypted and locked successfully ✔")
    exit()


# USER SECTION????????????????????????????????????????????????????????

if role == "user":
    print("\n[User mode]")

    channel_id = input("Enter channel number: ")
    if channel_id not in channels:
        print("Channel does not exist")
        exit()

    attempts = 0
    while attempts < 2:
        password = input("Enter password: ")
        pwd_hash = hash_password(password)

        if pwd_hash == channels[channel_id]["hash"]:
            print("\nAccess granted ✔")

            #  decrypte file function
            decrypted_content = decrypt_text(
                channels[channel_id]["encrypted_content"],
                channels[channel_id]["key"],
                channels[channel_id]["chars"]
            )

            #  read and print file content
            print("\n----- FILE CONTENT -----\n")
            print(decrypted_content)
            print("\n------------------------\n")

            #  print decrypted file
            decrypted_filename = "decrypted_" + channels[channel_id]["filename"]
            with open(decrypted_filename, "w", encoding="utf-8") as f:
                f.write(decrypted_content)

            print(f"Decrypted file saved as: {decrypted_filename}")
            exit()
        else:
            attempts += 1
            print("Wrong password")

    print("\nAccess denied ")
    exit()

