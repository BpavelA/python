from simplecrypt import *

with open('encrypted.bin', "rb") as e, open('passwords.txt', 'r') as p:
    encrypted = e.read()
    for i in p:
        try:
            print(decrypt(i.strip(), encrypted).decode('utf-8'))
        except:
            pass
