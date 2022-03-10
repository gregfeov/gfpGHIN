import socket
import tkinter
import time
s = socket.socket()
s.bind(("",9999))
s.listen(10) # Accepts up to 10 connections.
while True:
    sc, address = s.accept()
    print(address)
    f = open("C:\\users\\user\\documents\\ie.jpg",'wb') #open in binary
    while (True):
        l = sc.recv(1024)
        while (l):
            f.write(l)
            l = sc.recv(1024)
    f.close()
    print("Картинка получена!")

    sc.close()
s.close()