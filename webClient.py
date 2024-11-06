from socket import *
import sys
if len(sys.argv) <= 1:
    print('Usage: python client.py <server_ip> <port> <filename>')
    sys.exit(2)
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))
request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
client_socket.send(request.encode())
response = client_socket.recv(4096)
print("Server response:\n", response.decode())
client_socket.close()
