Server :
from socket import * serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) serverSocket.bind((gethostname(), serverPort)) print ("The server is ready to receive")
while 1:
sentence,clientAddress = serverSocket.recvfrom(2048)

file=open(sentence,"r") l=file.read(2048)

serverSocket.sendto(bytes(l,"utf-8"),clientAddress) print("sent back to client",l)
file.close()

Client :
from socket import * serverName = gethostname() serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

sentence = input("Enter file name") clientSocket.sendto(bytes(sentence,"utf-8"),(serverName, serverPort)) filecontents,serverAddress = clientSocket.recvfrom(2048)
print ('From Server:', filecontents) clientSocket.close()
