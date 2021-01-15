# Python code for the TCP server

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("The server is ready to receive.")

while True:

    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    # sentence2 = sentence.decode()
    capitalizedSentence = sentence.upper()
    print(capitalizedSentence)

    connectionSocket.sendto(capitalizedSentence.encode(),addr)

# connectionSocket.close()