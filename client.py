import socket
import threading

nickname = input('Choose a nickname: ')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.100.4', 9009))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print('Some error occurred')
			client.close()
			break