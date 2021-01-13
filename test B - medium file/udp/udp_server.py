import socket
import base64
from sys import getsizeof

BUFFER_SIZE = 512
FILENAME = 'data.txt'

def chunks(text, maxBufferSize):
    i = 0
    string = ''
    while i < maxBufferSize:
        string = string + '.'
        i = getsizeof(string)
    splitted = [text[0+m:len(string)+m] for m in range(0, len(text),len(string))]
    return splitted

toSend = open(FILENAME, 'rb').read()
lines = chunks(toSend,BUFFER_SIZE-100)
udpserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpserver.bind(("127.0.0.1", 20001))

print('UDP Server is running')

while(True):
    for num,line in enumerate(lines): 
        msg,ip = udpserver.recvfrom(BUFFER_SIZE)
        content_bytes = base64.encodebytes(line)
        udpserver.sendto(content_bytes, ip)
        print("CLIENT IP AND PORT:",ip)
        if(num == len(lines)-1):
            content_bytes = base64.encodebytes(str.encode('UDP SERVER'))
            msg,ip = udpserver.recvfrom(BUFFER_SIZE)
            udpserver.sendto(content_bytes, ip)
            print("CLIENT IP AND PORT:",ip)
