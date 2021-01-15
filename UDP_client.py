# Python code for the UDP client:

from socket import *
def main():
    serverName = 'localhost'

    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    try:
        clientSocket.connect((serverName, serverPort))
        print("Server Connected")
    except:
        print("Connection Error")

    
    while True :
        message = input("Input a lowercase sentence: ")
        if message == 'Quit':
            break
        else:
            # encoded_msg = message.encode()
            clientSocket.sendall(message.encode())
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print(modifiedMessage.decode())
    clientSocket.close()

main()
