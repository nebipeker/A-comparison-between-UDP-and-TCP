import socket

#ip address and port number for the connection
serverip = None
serverport = 12000

#creating a socket and listening for connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((serverIP, serverPort))
serversocket.listen(1)

	
while True:
    #accepting incoming connection
	clientsocket, address = serversocket.accept()
	
    clientsocket.send(bytes("Sending file...", "utf-8"))

    #will be filled later

    clientsocket.send(bytes('Transfer complete', 'utf-8'))

    #closing the connection
    clientsocket.close()