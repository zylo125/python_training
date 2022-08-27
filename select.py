#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

dbname = 'bils.db'
conn = sqlite3.connect(dbname)
conn.text_factory = str
cur = conn.cursor()
path = r'hoge/hogehoge/hogehogehoge/python'

for row in cur.execute('select * from bils'):
    area = row[0]
    huken = row[1]
    new_filepath = path + '/' + area + '/' + huken
    print(row[0], row[1], row[2])
    print(new_filepath)

conn.commit()
conn.close()