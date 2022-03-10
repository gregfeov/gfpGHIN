import socket
from co import *
def conne(i):
    ClientSocket = socket.socket()
    host = '192.168.1.64'
    port = 8081
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        return ("Troubles with server!")
        quit()
    while True:
        try:
            ClientSocket.send(str.encode("user:"+str(i)))
            Response = ClientSocket.recv(2048)
            resp=Response.decode('utf-8')
            return resp
            break
        except:
            print("Client except")
    ClientSocket.close()
def gb(ie):
    ClientSocket = socket.socket()
    host = '192.168.1.64'
    port = 8081
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        return ("Troubles with server!")
        quit()
    while True:
        try:
            ClientSocket.send(str.encode("balance:"+str(ie)))
            Response = ClientSocket.recv(2048)
            resp=Response.decode('utf-8')
            return resp
            break
        except:
            print("Client except")
    ClientSocket.close()