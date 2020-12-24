import socket

# Host ip adress and port
port = 8081
host = None

#Connection and saving location
s = socket.socket()
s.connect((host, port))
f = open("/Users/alpha/Desktop/CS447/test.txt",'wb')

#Getting data
while True:
    try:
        print("Receiving data...")
        data = s.recv(1024)
    except:
        print("Error at recieving!!")
    if not data:
        break
    print("Data=%s",  (data))
    f.write(data)