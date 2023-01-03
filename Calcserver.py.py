import socket
host=socket.gethostname()
port=6700
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind((host,port))
while True:
    data,addr=s.recvfrom(1024)
    data=data.decode("utf-8")
    result=eval(data)
    result=str(result).encode("utf-8")
    s.sendto(result,addr)