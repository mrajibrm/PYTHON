# Python code for the TCP client

from socket import *

def main():
    serverName = 'localhost'

    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    try:
        clientSocket.connect((serverName, serverPort))
        print("Server Connected")
    except:
        print("Connection Error")

    while True:
        sentence = input("Input a lowercase sentence: ")
        if sentence == 'Quit':
            break
        else:
            clientSocket.sendall(sentence.encode())

            modifiedSentence, serverAddress = clientSocket.recvfrom(1024)

            print(modifiedSentence.decode())

    clientSocket.close()

main()