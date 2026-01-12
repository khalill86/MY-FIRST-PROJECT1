#programe libraries 


import hashlib  # for hashing passwords
import json # for storing channel data
import time # for simulating loading
import os # for file operations
import random # for shuffling characters
import string # for character sets
def encrypt_text(text):
    characters = list(string.ascii_letters + string.digits + string.punctuation + " \n\t")
    #cette ligne  combine des lettres, des chiffres, des signes de ponctuation et des espaces en une seule liste de caractères.
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
#
print("Admin hash loaded")


ascii_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡈⠻⢿⣿⠿⣿⣿⣿⠇⣴⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⡆⠀⠀⠀⠀⠉⠀⢿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠙⢛⣉⣍⡛⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⣉⠛⣛⡉⠁⠀⠀⣀⣤⣶⣦⣤⣀⣶⠄⣿⣿⣿⣿⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠇⠀⠀⣸⠛⠉⠉⠙⣿⣿⣿⡆⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠟⠀⠀⠀⠁⠀⠀⠀⠀⢸⣿⣿⣿⣮⡻⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⢋⣩⣭⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣠⣶⡾⣿⣟⠛⣋⠁⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣩⣤⣶⣤⣄⡀⠀⢀⣼⣿⠟⠁⣩⣿⣿⢿⣿⡿⣽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢧⣾⣿⣿⣿⣿⣿⣿⡄⠻⠿⠁⢠⣾⣿⠟⣡⣾⣿⠛⢮⡛⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⢳⣾⣶⡄⠀⠈⢿⢸⣿⣿⣿⡟⣩⣶⣿⣿⣿⣷⣄⢿⡿⢫⣾⣿⣿⠏⣠⣼⡿⠾⣻⣽⣤⣶⡶⣦⣄⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⡿⠃⠈⠛⢿⣦⣀⣈⠈⢿⣿⡏⣼⣿⣿⣿⣿⣿⠿⣛⣂⣀⡛⢿⠟⣡⣾⣿⡿⢁⣾⣿⣿⣿⣿⡷⢹⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣼⡿⠋⠉⠀⠀⠀⠀⠀⠹⢿⣼⢧⡈⠻⠀⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⣿⣷⣄⢿⡟⠋⠀⣾⣿⣿⡿⠉⠩⠷⠿⣿⣿⣿⣿⡿⣫⣶⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⠋⠀⢠⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⣶⣶⣆⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠁⣀⣤⣶⣜⢿⠁⢸⣷⡄⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀
⠀⠀⠀⠀⣿⡇⠀⢰⣯⣿⠉⠉⢩⣍⣉⣉⣭⣭⣥⣭⣍⣻⣥⣭⣭⣜⠿⣿⣿⣿⣿⣿⣿⣿⠿⢓⠸⢿⣿⣿⡟⠀⠀⠀⢻⣧⣀⡀⠀⠈⠐⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⢀⣼⠿⠁⠀⢸⣿⡇⠀⢸⣿⠿⠟⠿⠿⠿⠿⢿⣿⣟⠛⠛⣻⣥⣴⣶⣄⠉⠛⠿⠟⢱⣿⣿⣿⡄⣀⠈⠀⠀⠀⠀⠈⠉⠛⠁⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⡇
⣠⡴⠟⠛⠁⠀⠀⢸⣿⡇⠀⣿⣿⠀⠀⢠⣼⣻⣿⣿⣿⣿⣿⣿⠾⣿⠿⠛⠁⣀⣴⣿⣷⠈⣛⠻⠟⠁⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢿⣿⡇⢀⣾⣿⡃⠉⠙⠛⠋⠁⠀⠀⠀⠀⠀⣟⡛⠻⣿⡁⠀⣿⣇⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠟⠿⠁⠀⢤⣤⣶⠆
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⢸⣿⡇⠸⣿⣿⡇⠀⠀⠀⣤⠾⠻⣿⣿⣶⣿⣿⣿⣦⠻⠃⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇⠀⠀⠀⢠⣼⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⢸⣶⠁⢐⡿⠏⠀⠀⠀⢠⣶⣿⣷⠘⠿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠋⠀⠀⠀⠀⣀⣼⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠜⠉⠀⠀⠀⢻⣧⠘⣿⣦⠀⠀⢠⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢀⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⠀⠘⣿⣧⠀⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠟⠀⠀⠀⣼⣿⠆⣿⣿⣿⣿⣿⢿⣿⣥⣴⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⠀⢹⣿⣿⡟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣤⣤⣤⣤⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠎⣿⣿⣿⣿⣿⣿⣿⣿⠟⣋⡉⠉⠛⠉⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⠟⠉⢼⣿⣿⣦⣆⢀⣠⣴⣦⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

print(ascii_art)
print("Welcome to Encryption Decryption Program")
all_charst=input("do you want to hash password or just encrypt it(h/e):   ") 
if all_charst.lower()=='h':    
    
    print("after hashing password you can't decrypt it back")  
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


    encrypted_content, key, chars = encrypt_text(file_content) # encrypt file content

  
    channels[channel_id] = {
        "hash": pwd_hash,
        "encrypted_content": encrypted_content,
        "key": key,
        "chars": chars,
        "filename": filename
    }

    save_channels(channels)


    with open(filename, "w", encoding="utf-8") as f: # overwrite original file
        f.write(encrypted_content) # write encrypted content to file

    print("\nFile encrypted and locked successfully ")
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
            print("\nAccess granted ")

            #  decrypte file function
            decrypted_content = decrypt_text(
                channels[channel_id]["encrypted_content"],
                channels[channel_id]["key"],
                channels[channel_id]["chars"]
            )

            #  read and print file content
            print("\n FILE CONTENT -\n")
            print(decrypted_content)
            print("\n--\n")

            #  print decrypted file
            decrypted_filename = "decrypted_" + channels[channel_id]["filename"]
            with open(decrypted_filename, "w", encoding="utf-8") as f:
                f.write(decrypted_content)

            print(f"Decrypted file saved as: {decrypted_filename}")
            exit()
        else:
            attempts += 1
            print("Wrong password")

    print("\n Access denied ")
    exit()

