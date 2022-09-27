# TCP Server

# import socket
# s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 9999

# s.bind(host , port)
# s.listen(5)
# while(True):
#     conn,adrr = s.connect()
#     print(f'got conn from {adrr}')
#     conn.send("aaaaa")
#     conn.close()


# UDP Server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 9999

s.bind((host, port))

while(True):
    data, adr = s.recvfrom(1024)
    print(data, adr)
