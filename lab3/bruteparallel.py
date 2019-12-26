#!/usr/bin/python

from threading import Thread
from zipfile import ZipFile
import itertools

def decart(ls):
    return list(itertools.product(*ls)) 

found = False
def brute(t,y):
    with ZipFile('zzz.zip') as b:
        for i in range(t, y): 
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
                
thread1 = Thread(target=brute, args=(1,2))
thread2 = Thread(target=brute, args=(3,4))
thread3 = Thread(target=brute, args=(5,6))

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
