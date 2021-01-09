import socket
import base64

BUFFER_SIZE = 512

content_bytes = base64.encodebytes(str.encode("UDP SERVER LISTENING"))
udpserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpserver.bind(("127.0.0.1", 20005))

print("sadassfasfsfda")
while(True):
    msg,ip = udpserver.recvfrom(BUFFER_SIZE)
    udpserver.sendto(content_bytes, ip)
    print("UDP CLIENT MESSAGE:",msg)
    print("CLIENT IP:",ip)
    

