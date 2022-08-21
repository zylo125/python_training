#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue

path = "/hoge/hogehoge/hogehogehoge/python/"
huken = ['osaka','tokyo','kanagawa']
q = queue.Queue()

for i in huken:
    q.put(i)

while not q.empty():
    filepath = path + '/' + q.get() + '.txt'
    print(filepath)