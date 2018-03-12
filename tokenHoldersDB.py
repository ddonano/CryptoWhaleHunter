# -*- coding: UTF-8 -*-
# @yasinkuyu

import os
import sqlite3
# Define Custom import vars
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tokenHolders.db')
conn = sqlite3.connect(path, check_same_thread=False)

# db desc
class tokenHoldersDB():


    # Database (Todo: Not complated)
    @staticmethod
    def create(sqlname):
        # Address, Quantity
        cur = conn.cursor()
        cur.execute('''CREATE TABLE if not exists ''' + sqlname + ''' (Rank INT PRIMARY KEY UNIQUE,Address  STRING,Quantity DOUBLE)''')

    @staticmethod
    def write(sqlname, rank, address, quantity):
        '''
        Save order
        data = TxHash, Age, From, To, Quantity
        Create a database connection
        '''
        cur = conn.cursor()
        cur.execute('''INSERT INTO ''' + sqlname + ''' VALUES (?, ?,?)''', (rank, address, quantity,))
        conn.commit()

    @staticmethod
    def update(sqlname, rank, address, quantity):
        cur = conn.cursor()
        cur.execute('''REPLACE INTO ''' + sqlname + ''' VALUES (?, ?,?)''', (rank, address, quantity,))
        conn.commit()

    @staticmethod
    def read(sqlname, rank):
        '''
        Query order info by TxHash
        :param txHash
        :return:
        '''
        cur = conn.cursor()
        cur.execute('''SELECT * FROM ''' + sqlname + ''' WHERE Rank=?''', (rank,))
        return cur.fetchone()

    @staticmethod
    def readfromaddress(sqlname, address):
        '''
        Query order info by TxHash
        :param txHash
        :return:
        '''
        cur = conn.cursor()
        cur.execute('''SELECT * FROM ''' + sqlname + ''' WHERE Address=?''', (address,))
        return cur.fetchone()
