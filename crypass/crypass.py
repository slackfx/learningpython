#!/usr/bin/env python
from db.database import DatabaseEntry
from db.db_to_csv import write_csv
from encrypter.Encrypter import CryptoAES

import csv
import os

def read(filename):
    with open(filename, 'rb') as csvfile:
        for r in csvfile:
            print(r)
    print('-' * 100)

if __name__ == '__main__':
    db = [
            DatabaseEntry(name='google', url='www.google.com', username='teste@gmail.com', password='123'),
            DatabaseEntry(name='orkut', url='www.google.com', username='teste@gmail.com', password='123'),
            DatabaseEntry(name='bate papo uol', url='batepapo.uol.com.br', username='teste@uol.com', password='123'),
            DatabaseEntry(name='facebook', url='www.facebook.com', username='teste@gmail.com', password='123'),
    ]
    dbname = 'mydb.csv'
    write_csv(db, dbname)

    read(dbname)

    crypt = CryptoAES()

    password = crypt.digest_password('qwe123')

    crypt.encrypt_file(password, dbname)

    read(dbname)

    crypt.decrypt_file(password, dbname)

    #read(dbname)

    with open(dbname, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        db2 = []
        for row in reader:
            db2.append(DatabaseEntry(row[0], row[1], row[2], row[3]))

        for x in db2:
            print('Name:', x.name)
            print('URL:', x.url)
            print('Username:', x.username)
            print('Password:', x.password)
            print('#' * 50)

    os.remove(dbname)
