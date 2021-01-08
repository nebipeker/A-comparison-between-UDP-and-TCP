import socket
import base64

FILENAME = 'zoo.txt'

file_content = open('zoo.txt', 'rb').read()
content_bytes = base64.encodebytes(file_content)
udpserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpserver.bind(("127.0.0.1", 20001))

while(True):
    msg,ip = udpserver.recvfrom(1024)
    udpserver.sendto(content_bytes, ip)
    print("UDP CLIENT MESSAGE:",msg)
    print("CLIENT IP:",ip)