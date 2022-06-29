#TCP Server
import socket

s = socket.socket()
host = socket.gethostname()
port = 3000

s.bind((host, port))

s.listen(5)

while True:
    conn,addr = s.accept()
    print('got conn from ', addr)
    conn.send("server: hi bruda")
    conn.close()