import socket
host=socket.gethostname()
port=6000
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind((host,port))

msg,addr=s.recvfrom(1024)
msg=msg.decode("utf-8")
file=open("Dhan.txt","w")
file.write(msg)
file.close()