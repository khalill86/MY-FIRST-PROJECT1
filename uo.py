import hashlib
import os
import random
import string
import json
from colorama import Fore, Style, init

init(autoreset=True)

# ==========================
# Configuration
# ==========================
DATA_FILE = "channels.json"

# ==========================
# Helper functions
# ==========================
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

# ==========================
# ASCII Art
# ==========================
ascii_art = r"""
S%t%X@SXSSXXXXSXSS@XSXX%X
XX88@X8@@@@@@@@@8888888@@
@;;%XXSXSXSXSSSSXXS8@%ttS
 ;S;88@88888888@88888t%S
 @;tS8@888888@888@@8tS;8
 X;tS8@@@@88@@@@@@8%X;t8
 StSt88@@@88@@@8@@X8ttt@
"""

# ==========================
# Program start
# ==========================
print(Fore.RED + ascii_art + Style.RESET_ALL)
print("Welcome 👋")

channels = load_channels()

role = input("Do you want to login as user or admin? (u/a): ").lower()

if role in ("a", "admin"):
    role = "admin"
elif role in ("u", "user"):
    role = "user"
else:
    print("Invalid choice")
    exit()

# ==========================
# ADMIN SECTION
# ==========================
if role == "admin":
    print("\n[Admin mode]")

    filename = input("Enter the file name: ")
    if not os.path.exists(filename):
        print("File not found")
        exit()

    channel_id = input("Enter channel number: ")
    password = input("Set a password for this channel: ")

    pwd_hash = hash_password(password)
    encrypted, key, characters = encrypt_password(password)

    channels[channel_id] = {
        "hash": pwd_hash,
        "encrypted": encrypted,
        "key": key,
        "chars": characters,
        "file": filename
    }

    save_channels(channels)

    print("\nOperation completed successfully ✔")
    exit()

# ==========================
# USER SECTION
# ==========================
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

            real_password = decrypt_password(
                channels[channel_id]["encrypted"],
                channels[channel_id]["key"],
                channels[channel_id]["chars"]
            )

            print("File:", channels[channel_id]["file"])
            print("Decrypted password:", real_password)
            exit()
        else:
            attempts += 1
            print("Wrong password")

    print("\nAccess denied ✖")
    exit()
    print("You chose not to decrypt the message.")