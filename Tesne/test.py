#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-10-17 17:29:09

import pymysql
import time

start = time.time()
conn = pymysql.connect(host='127.0.0.1', user='dear', password='both-win', db='cmdb')
cursor = conn.cursor()
# sql = 'select * from test;'
sql = 'insert into test (id, title, author) value (0,2,3);'

for i in range(10000):
    cursor.execute(sql)
    data = cursor.fetchall()

conn.commit()

cursor.close()
conn.close()
print(time.time() - start)
