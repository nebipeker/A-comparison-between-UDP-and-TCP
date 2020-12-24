import socket

#ip address and port number for the connection
<<<<<<< HEAD
serverip = ''
=======
serverip = '85.103.110.149'
>>>>>>> 5f1585a361933711cdbd14b8f707f048a9c0af89
serverport = 12000

#creating a socket and listening for connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((serverip, serverport))
serversocket.listen(1)

	
while True:
    #accepting incoming connection
	clientsocket, address = serversocket.accept()
<<<<<<< HEAD
=======

    #print('Connected to {adress}'.format(adress))
>>>>>>> 5f1585a361933711cdbd14b8f707f048a9c0af89
	
    clientsocket.send(bytes('Sending file...', 'utf-8'))

    filename = 'data.txt' #must be in the same folder with tcp-server.py
    testfile = open(filename, 'rb') #r is for reading and b is for binary, 'reading binary file'
    #read the next 1024 bytes from the file
    data = testfile.read(1024)
    #when there is data left send it
    while (data):
       clientsocket.send(data)
       data = testfile.read(1024)
    testfile.close()
    print('File is sent')

    clientsocket.send(bytes('Transfer complete', 'utf-8'))

    #closing the connection with client
    clientsocket.close()