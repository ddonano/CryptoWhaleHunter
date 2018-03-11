# -*- coding: UTF-8 -*-
# @yasinkuyu

import os
import sqlite3
# Define Custom import vars
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'txs.db')
conn = sqlite3.connect(path, check_same_thread=False)

class dataBase():

    # Database (Todo: Not complated)
    @staticmethod
    def create(sqlname):
        # TxHash, Age, From, To, Quantity
        cur = conn.cursor()
        cur.execute('''CREATE TABLE if not exists ''' +sqlname +''' (TxHash  STRING PRIMARY KEY UNIQUE,Age STRING,`From` STRING,`To` STRING,Quantity DOUBLE)''')

    @staticmethod
    def write(sqlname, tx, time, send, rev, qua):
        '''
        Save order
        data = TxHash, Age, From, To, Quantity
        Create a database connection
        '''
        cur = conn.cursor()
        cur.execute('''INSERT INTO ''' + sqlname + ''' VALUES (?, ?, ?, ?, ?)''', (tx, time, send, rev, qua,))
        conn.commit()

    @staticmethod
    def read(sqlname, txHash):
        '''
        Query order info by TxHash
        :param txHash
        :return:
        '''
        cur = conn.cursor()
        cur.execute('''SELECT * FROM ''' + sqlname + ''' WHERE `TxHash`=?''', (txHash,))
        return cur.fetchone()
