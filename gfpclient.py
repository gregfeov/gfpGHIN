import socket
from co import *

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 8081
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(r("Troubles with server!"))
    quit()
while True:
    i = input('Enter message: ')
    try:
        ClientSocket.send(str.encode(i))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    except:
        print(r("Server stopped!"))
    if i == "quit":
        ClientSocket.send(str.encode("Client exit"))
        exit(1)
ClientSocket.close()