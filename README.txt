All tree tests A,B and C have their own udp and tcp files
codes are identical, what difers is the content of the data.txt file 

form A to C data's size increases. 

To observe the transmission you will need to begin scanning with the wireshark before you begin the transmission.

to execute the udp and tcp classes you'll need python 3.9.0.

You can execute these by going to the directory of them using cmd and typing python filename.py 
which will execute the class. 

to correctly complete the file transfrers, for both udp and tcp file pairs, you must first execute the udp_server.py or the tcp_server.py which will stand by. Then you can exacute the client part of the pair. 

Once a pair is correctly started up they will begin transmitting data.txt file . 

The transmission will be observeble from Wireshark. 
