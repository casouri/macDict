#!/usr/bin/python3

import sqlite3
from os import walk, environ, path
import glob
import yaml

# sqlite_file = '/Users/yuan/Library/Dictionaries/CoreDataUbiquitySupport/yuan~7816679D-5DC8-5BDE-9F6C-EB46C69CAF78/UserDictionary/11C74B55-EDA1-4B9E-8EE6-F5E00D19A3B9/store/UserDictionary.db'

DIR_PATH = path.dirname(__file__)

# find database file path
file_list = glob.glob(
    environ['HOME'] +
    '/Library/Dictionaries/CoreDataUbiquitySupport/**/UserDictionary.db',
    recursive=True)
db_path = file_list[0]


# read dictionary
with open('dict.yml') as stream:
    dictionary = yaml.load(stream)


def i(dictionary):
    # manipulate database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for dic in dictionary:
        c.execute(
            "INSERT INTO `ZUSERDICTIONARYENTRY`(`Z_PK`,`Z_ENT`,`Z_OPT`,`ZAUXINTVALUE1`,`ZAUXINTVALUE2`,`ZAUXINTVALUE3`,`ZAUXINTVALUE4`,`ZTIMESTAMP`,`ZAUXSTRINGVALUE1`,`ZAUXSTRINGVALUE2`,`ZAUXSTRINGVALUE3`,`ZAUXSTRINGVALUE4`,`ZPARTOFSPEECH`,`ZPHRASE`,`ZSHORTCUT`,`ZAUXDATAVALUE`) VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'{phase}','{short_cut}',NULL);".
            format(phase=dic['with'], short_cut=dic['replace']))
    # close and save
    c.close()
    conn.commit()
    conn.close()


def d(dictionary):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for dic in dictionary:
        c.execute(
            "DELETE FROM ZUSERDICTIONARYENTRY WHERE ZPHRASE = '{phase}';".
            format(phase=dic['with']))
    # close and save
    c.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    print('\n"i" for inserting text substitutions\n"d" for removing them\n"q" for quit\n')
    while True:
        ipt = input('>>> ')
        if ipt == 'q':
            break
        elif ipt == 'i':
            i(dictionary)
        elif ipt == 'd':
            d(dictionary)
        else:
            print('\ninvalid command\n')
