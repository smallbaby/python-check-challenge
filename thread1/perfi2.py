# requests/sec of fast request

from socket import *
import time


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

from threading import Thread
n=0
def monitor():
	while True:
		global n
		time.sleep(1)
		print(n, 'requ/sec')
		n = 0
Thread(target=monitor).start()

while True:
	sock.send(b'1')
	resp = sock.recv(100)
	n += 1





	
