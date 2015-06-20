# -*- coding: utf-8
"""
Главный скрипт проекта.
"""
import os
from grab import Grab
import datetime
import time

x = [2,6,10,14,18,22]
c = []
dat = {2:0,6:0,10:0,14:0,18:0,22:0}
g = Grab()
now_time = datetime.datetime.utcnow()
day = now_time.day

while True:
    now_time = datetime.datetime.utcnow()
    h = now_time.hour
    if h in x:
        if h in c:
            o = 0
        else:
            g.go("https://webtransfer-finance.com/ru/page/about")
            proc = g.doc.rex_text('<span class="right">([^>]+)%</span>')
            c.append(h)
            dat[h]=float(proc)
    if day< now_time.day:
        os.popen('python gra.py '+str(dat[2])+' '+str(dat[6])+' '+str(dat[10])+' '+str(dat[14])+' '+str(dat[18])+' '+str(dat[22]))
        c = []
        dat = {2:0,6:0,10:0,14:0,18:0,22:0}
        day = now_time.day
    time.sleep(60)


