import os, random, struct
from Crypto.Cipher import AES
from Crypto import Random
import hashlib

class PasswordNotMatchException(Exception):
    pass

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    iv = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            outfile.write(key)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.out'
    
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        stored_hash = infile.read(32)
        if stored_hash != key:
            raise PasswordNotMatchException('password don\'t match')

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)

password = 'qwe123'
password2 = '123qwe'
k = hashlib.sha256(password.encode('utf-8')).digest()
k2 = hashlib.sha256(password2.encode('utf-8')).digest()
encrypt_file(k, 'encode.txt')

decrypt_file(k, 'encode.txt.enc')
