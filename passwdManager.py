from Crypto.Cipher import AES 
from Crypto import Random 
import binascii


def append_space_padding(str, blocksize=128):
    pad_len = blocksize - (len(str) % blocksize)
    padding = 'a'*pad_len
    return str + padding


def remove_space_padding(str, blocksize=128):
    pad_len = 0

    for char in str[::-1]:
        if char == 'a':
            pad_len += 1
        else:
            break

    return str[:-pad_len]


def encrypt(plain, u):
    plaintext = append_space_padding(plain)
    key = Random.new().read(16)
    try:
        with open('key.key', 'rb') as file:
            key = file.read()
    except FileNotFoundError:
        with open('key.key', 'wb') as file:
            file.write(key)

    aes = AES.new(key, AES.MODE_ECB)
    if(u == 'u'):
        with open('username.enc', 'wb') as file:
            file.write(aes.encrypt(plaintext.encode('UTF-8')))
    elif(u == 'p'):
        with open('password.enc', 'wb') as file:
            file.write(aes.encrypt(plaintext.encode('UTF-8')))
    
    return aes.encrypt(plaintext.encode('UTF-8'))


def generateKey():
    key = Random.new().read(16)
    with open('key.key', 'wb') as file:
        file.write(key)


def decrypt(u):
    key = Random.new().read(16)
    try:
        with open('key.key', 'rb') as file:
            key = file.read()
    except FileNotFoundError:
        with open('key.key', 'wb') as file:
            file.write(key)

    aes = AES.new(key, AES.MODE_ECB)
    ciphertext = b''

    if(u == 'u'):
        with open('username.enc', 'rb') as file:
            ciphertext = file.read()
    elif(u == 'p'):
        with open('password.enc', 'rb') as file:
            ciphertext = file.read()
    
    decrypted = aes.decrypt(ciphertext).decode('UTF-8')
    return remove_space_padding(decrypted)


key = Random.new().read(16)
try:
    with open('key.key', 'rb') as file:
        key = file.read()
except FileNotFoundError:
    with open('key.key', 'wb') as file:
        file.write(key)
