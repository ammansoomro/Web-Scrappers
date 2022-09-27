# Encryption and Decryption of a file using AES-256

import os
import sys
import base64
import hashlib
import argparse
from Crypto import Random
from Crypto.Cipher import AES

# AES-256 Encryption
def encrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = "(encrypted)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, "rb") as infile:
        with open(outputFile, "wb") as outfile:
            outfile.write(filesize.encode("utf-8"))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b" " * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

# AES-256 Decryption
def decrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename[11:]

    with open(filename, "rb") as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(filesize)
        
# Main Function
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="encrypt or decrypt")
    parser.add_argument("file", help="file to encrypt or decrypt")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("The file does not exist!")
        sys.exit(1)

    password = "password"
    key = hashlib.sha256(password.encode("utf-8")).digest()

    if args.action == "encrypt":
        encrypt(key, args.file)
        print("Done.")
    elif args.action == "decrypt":
        decrypt(key, args.file)
        print("Done.")
    else:
        print("No action specified!")
    
if __name__ == "__main__":
    Main()

