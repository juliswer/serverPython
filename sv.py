# Creating a server with python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8000))
server.listen()

sock, address = server.accept()
data = sock.recv(1024)
print(data)

sock.close()
server.close()
