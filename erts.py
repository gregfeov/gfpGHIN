import socket
import os
from _thread import *
from co import *
from gfplib import *
ServerSocket = socket.socket()
host = ''
port = 8081
ThreadCount=0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(1000)
def threaded_client(connection):
    while True:
        try:
            data = connection.recv(2048)
            m = data.decode('utf-8')
            aske = m.split(":", 2)
            print(aske[0]+aske[1])
            if aske[0] == "user":
                try:
                    confirmedpassword = getpassword(str(aske[1]))
                    connection.sendall(str.encode(confirmedpassword))
                except:
                    connection.sendall(str.encode("User can't be find!"))
            else:
                connection.sendall(str.encode("Wait a command"))
            if aske[0] == "balance":
                print(aske[1])
                confirmedbalance = getbalance(str(aske[1]))
                print(confirmedbalance)
                connection.sendall(str.encode(confirmedpassword))
            else:
                connection.sendall(str.encode("Wait a commandee"))
        except:
            print("Client disconnected!")
            break
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print(cy('Client address: ') + cy(address[0] + ':' + str(address[1])))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print(cy('Client id: ' + str(ThreadCount)))
    print(31*"-")
ServerSocket.close()