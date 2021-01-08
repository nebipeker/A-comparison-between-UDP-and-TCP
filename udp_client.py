import socket
import base64

udpclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpclient.sendto(str.encode("UDP MESSAGE"), ("127.0.0.1", 20001))
message = udpclient.recvfrom(1024)
message_bytes = base64.b64decode(message[0])
print((message_bytes.decode('ascii')))