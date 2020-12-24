import socket


# Host ip adress and port
port = 12000
host = "192.168.56.1"

#Connection and saving location
socket_ = socket.socket()
socket_.connect((host, port))
f = open("/Users/alpha/Desktop/CS447/test.txt",'wb')

#Getting data
while True:
    try:
        print("Receiving data...")
        data = socket_.recv(1024)
    except:
        print("Error at recieving!!")
    if not data:
        break
    print("Data=",data)
    f.write(data)