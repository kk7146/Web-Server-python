from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive on port", serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print("Received request:", message)
        filename = message.split()[1]
        with open(filename[1:], 'r') as f:
            outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.sendall(outputdata.encode())
    except IOError:
        try:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        except BrokenPipeError:
            print("Client disconnected before sending 404 response")
    except BrokenPipeError:
        print("Client disconnected before sending data")
    finally:
        connectionSocket.close()
serverSocket.close()
sys.exit()
