#TCP client
# import socket
# s = socket.socket()
# host = socket.gethostname()
# port = 9999
# s.connect(host, port)

# print(s.recv(1024))
# s.close()

#udp

import socket
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

host = socket.gethostname()
port = 9999

msg = 'test'

s.sendto(msg , (host , port))