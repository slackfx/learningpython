import hashlib, os, random, struct
from Crypto.Cipher import AES
from Crypto import Random

class CryptoAES:
    CHUNK_SIZE = 64 * 1024
    IV_SIZE = 16

    def encrypt_file(self, key, filename):
        out_filename = filename + '.tmp'
        iv = self._generate_random_IV()

        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(filename)

        with open(filename, 'rb') as file_:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)

                while True:
                    chunk = file_.read(self.CHUNK_SIZE)
                    chunk_len = len(chunk)

                    if chunk_len == 0:
                        break
                    elif chunk_len % 16 != 0:
                        chunk += b' ' * (16 - chunk_len % 16)

                    outfile.write(encryptor.encrypt(chunk))
            os.remove(filename)
            os.rename(out_filename, filename)

    def decrypt_file(self, key, filename):
        out_filename = filename + '.tmp'
        with open(filename, 'rb') as file_:
            original_size = struct.unpack('<Q', file_.read(struct.calcsize('Q')))[0]
            iv = file_.read(self.IV_SIZE)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = file_.read(self.CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(original_size)
            os.remove(filename)
            os.rename(out_filename, filename)

    def digest_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).digest()

    def _generate_random_IV(self):
        return Random.new().read(self.IV_SIZE)
