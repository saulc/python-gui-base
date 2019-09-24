
import socket

# https://realpython.com/python-sockets/
# echo server/client bare min for socet send/Received

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print('Received', repr(data))
    
    s.sendall(b'Back for more')
    data = s.recv(1024)
    print('Received', repr(data))
