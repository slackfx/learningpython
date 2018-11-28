from Crypto.Cipher import AES

import hashlib

password = 'kitty'
key = hashlib.sha256(password.encode('utf-8')).digest()
print(key)
#key = '0123456789abcdef'
IV = 16 * '\x00'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = 'j' * 64 + 'i' * 128
ciphertext = encryptor.encrypt(text)

print(IV)
print(ciphertext)
print('-' * 100)
print(encryptor.decrypt(ciphertext))
