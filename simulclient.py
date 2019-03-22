import socket

HOST = '192.168.1.28'  # The server's hostname or IP address
PORT = 9999        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'D4F55GD44DF401')
    data = s.recv(1024)

print('Received', repr(data))