import threading
import socket

host = '192.168.100.4'
port = 9009

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)

def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} has lest the chatroom')
			nicknames.remove(nickname)
			break

def receive():
	while True:
		client, address = server.accept()
		print(f'Connected with {str(address)}')
		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)
		print(f'Nickname of the client is {nickname}!')
		broadcast(f'{nickname} joined the chatroom!'.encode('ascii'))
		cliend.send('Connected to the server. Now you can chat!'.encode('ascii'))
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

print('Server is listening')
receive()



