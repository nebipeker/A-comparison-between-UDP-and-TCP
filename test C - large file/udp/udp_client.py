import socket
import base64
from sys import getsizeof

FILENAME = 'data.txt'
BUFFER_SIZE = 512

def chunks(text, maxBufferSize):
    i = 0
    string = ''
    while i < maxBufferSize:
        string = string + '.'
        i = getsizeof(string)
    print(text)
    splitted = [text[0+m:len(string)+m] for m in range(0, len(text),len(string))]
    return splitted

toSend = open(FILENAME, 'rb').read()

lines = chunks(toSend,BUFFER_SIZE)

for line in lines:
    udpclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udpclient.sendto(line, ("127.0.0.1", 20001))
    message = udpclient.recvfrom(BUFFER_SIZE)
    message_bytes = base64.b64decode(message[0])
    print((message_bytes.decode('ascii')))
