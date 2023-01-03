import socket
host=socket.gethostname()
port=6700
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
addr=(host,port)
while True:
    print("Enter the equation")
    equation=input()
    equation=equation.encode("utf-8")
    s.sendto(equation,addr)
    data,addr=s.recvfrom(1024)
    data=data.decode()
    print("Result is:",data)
