import socket
#ip address and port number for the connection
serverip = ''
serverport = 12000

    #creating a socket and listening for connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((serverip, serverport))
serversocket.listen(1)


while True:
    print('Listening for incoming connections...')
    #accepting incoming connection
    clientsocket, address = serversocket.accept()

    print('Sending file...')

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
        
    #closing the connection with client
    clientsocket.close()