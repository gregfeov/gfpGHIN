import socket
import os.path
s = socket.socket()
s.connect(("127.0.0.1", 9999))
f = open("C:\\users\\user\\documents\\i.jpg", "rb")
b=os.path.getsize("C:\\users\\user\\documents\\i.jpg")
print(b)
l = f.read(b)
while (l):
    s.send(l)
    print(l)
    l = f.read(b)
s.close()