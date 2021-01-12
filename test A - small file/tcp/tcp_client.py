import socket

    # Host ip adress and port
port = 12000
host = '127.0.0.1'

#Connection and saving location
socket_ = socket.socket()
socket_.connect((host, port))
f = open("output.txt", 'wb')
print("Transfer initiated")

#Getting data
while True:
    try:
        data = socket_.recv(1024)
    except:
        print("Error! Transfer failed")
    if not data:
        print("Transfer complete")
        break
    f.write(data)