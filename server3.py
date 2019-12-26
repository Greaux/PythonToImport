import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 10005))
sock.listen(1)
while True:
	conn, _ = sock.accept()
	data = conn.recv(1024)
	if not data:
		break
	data = data.rstrip()
	output= subprocess.check_output(data, shell=True)
	conn.sendall(output)
	conn.close()
