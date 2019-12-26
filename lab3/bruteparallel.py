#!/usr/bin/python

import threading
from zipfile import ZipFile
import itertools

def decart(ls):
    return list(itertools.product(*ls)) 

found = False
with ZipFile('zzz.zip') as b:
    for i in range(1, 5): 
        sym = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        passw = map(lambda x: ''.join(x), decart([sym] * i))
        for password in passw:
            try:
                b.extractall(pwd=password)
                print 'Password: ' + password
                found = True
                break
            except:
                pass
        if found:
            print
