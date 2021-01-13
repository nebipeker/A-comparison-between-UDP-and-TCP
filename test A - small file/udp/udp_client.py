import socket
import base64

BUFFER_SIZE = 512
f = open("output.txt", 'wb')
message_bytes = bytes()

while(message_bytes.decode('latin1')!="UDP SERVER"):
    udpclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udpclient.sendto(str.encode("UDP CLIENT MESSAGE"),("127.0.0.1", 20001))
    message = udpclient.recvfrom(BUFFER_SIZE)
    message_bytes = base64.b64decode(message[0])
    f.write(message_bytes)
f.close()
print('File received')