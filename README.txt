# A comparison between UDP and TCP

This report aims to compare the Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) transport layer protocols used for transmitting application layer messages through computer networks. It analyzes and investigates these protocols and conducts tests to observe how differing transmission sizes affect both protocols and how they differ from each other in practice.

## Setup

The project team has created two pairs of Python code for TCP and UDP using the latest Python library, Python 3.9.0, and the socket.py interface. The UDP pair uses an additional interface, base64.py, to turn test data into a format that UDP can transmit across. Each pair consists of a client and server class that transmits a text file between the ports created by these classes. The team uses the latest version of Wireshark to track the data packets coming and going from the sockets and the addresses.

## Testing

The team conducts tests on both TCP and UDP to observe how these protocols react to varying data sizes. Tests A, B, and C use 2KB, 156KB, and 1.790KB .txt files to be transmitted, respectively. The team also creates an output.txt file upon successful transmission, filling it with the delivered data to detect any corruption during transmission. The tests are conducted on a machine with Windows 10 OS, and Wireshark is used to observe the packets sent to the specific ports. The team expects UDP to be less reliable than TCP, with a number of packets lost during their transportation due to various circumstances of the network they are transmitted through.



## Conclusion

In conclusion, the report successfully compares TCP and UDP by conducting tests on both protocols using varying data sizes. The team observes that TCP is more reliable than UDP but slower in transmission. UDP is faster but less reliable than TCP. Both protocols have their advantages and disadvantages and should be used according to specific transmission requirements.
