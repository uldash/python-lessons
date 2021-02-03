from simplecrypt import *

passwords = open('passwords.txt', 'r')
with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()
    for password in passwords:
        try:
            str = decrypt(password.strip(), encrypted)
        except:
            pass
        else:
            print(str)
passwords.close()
