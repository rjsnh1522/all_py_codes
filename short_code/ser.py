import socket
import sys
import threading

host = ''
port = 8888

s = socket.socket(scoket.AF_INET, socket.SOCK_STREAM)

print(s)

try:
	s.bind(host, port)
except socket.error:
	print("Binding failed")
	sys.exit()


print("sock has been bounded")
s.listen(10)

print("socket is ready")

def clientthread(conn):
	conn.send("Welcome")

	while True:
		data = conn.recv(1024)
		reply = "ok "+ data.decode()
		if not data:
			break
		print(reply)
		conn.sendall(reply)
	conn.close()





while 1:
	conn, addr = s.accept()
	print("connected with "+addr[0]+ ":" + str(addr[1]))


conn.close()
s.close()







