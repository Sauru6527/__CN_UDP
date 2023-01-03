import socket
host=socket.gethostname()
port=6000
addr=(host,port)
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
file=open("Dhanu.txt","r")
msg=file.read()
msg=msg.encode("utf-8")
s.sendto(msg,addr)

