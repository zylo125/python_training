#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

dbname = 'bils.db'
conn = sqlite3.connect(dbname)
conn.text_factory = str
cur = conn.cursor()

cur.execute(
    'CREATE TABLE IF NOT EXISTS bils(chiku STRING, huken STRING, bill STRING)')

sql = 'INSERT INTO bils(chiku, huken, bill) VALUES(?,?,?)'
data = ['九州_沖縄','福岡','福岡ビル']
cur.execute(sql,data)

cur.execute('select * from bils')
result = cur.fetchall()
print(result)

conn.commit()
conn.close()