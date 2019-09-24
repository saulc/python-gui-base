import socket
# https://docs.python.org/3/howto/sockets.html
# https://realpython.com/python-sockets/
# echo server/client bare min for socet send/Received
# sites aboved used as reference.

class ssocket:
    def __init__(self, blah):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def setupServer(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen()
        conn, addr = self.sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                print('Message Received: ' + str(data))


    def msend(self, msg):
        pass

    def mreceive(self):
        pass
