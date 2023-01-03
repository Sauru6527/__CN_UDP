import socket

localIp=socket.gethostname()
localPort = 20001
msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIp, localPort))
print("UDP server up and listening")
while (True):
    message,address = UDPServerSocket.recvfrom(1024)
    message=message.decode("utf-8")
    print("Message from Client:")
    print(message)
    print("Enter message to client:")
    data=input()
    data=data.encode("utf-8")
    UDPServerSocket.sendto(data, address)
