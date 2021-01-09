import socket
import base64

from sys import getsizeof

def chunks(maxBufferSize, listOfLines):
    toSend = []
    while listOfLines:
        if(toSend):
            if((getsizeof(listOfLines[0])+getsizeof(toSend[-1])) <= maxBufferSize):
                toSend[-1] = toSend[-1] + listOfLines.pop(0)
            else:
                toSend.append(listOfLines.pop(0))
        else:
            toSend.append(listOfLines.pop(0))
    return toSend

FILENAME = 'zoo.txt'
BUFFER_SIZE = 512

with open(FILENAME) as f:
    lines = f.readlines()

groupLines = chunks(BUFFER_SIZE, lines)

for line in groupLines:
    udpclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udpclient.sendto(str.encode(line), ("127.0.0.1", 20001))
    message = udpclient.recvfrom(BUFFER_SIZE)
    message_bytes = base64.b64decode(message[0])
    print((message_bytes.decode('ascii')))