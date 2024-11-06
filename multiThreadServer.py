from socket import *
import threading
serverPort = 6789
def handle_client(connectionSocket):
    message = connectionSocket.recv(1024).decode()
    filename = message.split()[1]
    with open(filename[1:], 'r') as f:
        outputdata = f.read()
    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    connectionSocket.sendall(outputdata.encode())
    connectionSocket.close()
def start_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"The server is ready to receive on port {serverPort}")
    while True:
        connectionSocket, addr = serverSocket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
