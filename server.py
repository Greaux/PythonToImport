#!/usr/bin/python

import hashlib
import socket as sck

def store(d):
    with open('/tmp/out', 'a+') as h:
        h.write(d + "\n")

def encrypt(p):
    return hashlib.sha512(p).hexdigest()

sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
sock.bind(('127.0.0.1', 10001))
sock.listen(1)
while True:
    conn, _ = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.rstrip()
        login, passwd = data.split(' ')
        store(login + ' ' + encrypt(passwd))
    conn.close()

# connect via client:
# telnet 127.0.0.1 10001
# aaa bbb
# ^]
# ^D

# ps aux | grep python
# 1030
# pyrasite-shell 1030
# def encrypt(p):
#     return p
