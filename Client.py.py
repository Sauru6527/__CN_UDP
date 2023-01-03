import socket
serverAddressPort = ("127.0.0.1", 20001)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while True:
    print("Enter message to sent:")
    data=input()
    data=data.encode("utf-8")
    UDPClientSocket.sendto(data, serverAddressPort)
    msgFromServer,addr = UDPClientSocket.recvfrom(1024)
    msgFromServer=msgFromServer.decode("utf-8")
    print("Message from server:",msgFromServer)
    print(msgFromServer)

