import socket
# https://docs.python.org/3/howto/sockets.html
# https://realpython.com/python-sockets/
# echo server/client bare min for socet send/Received
# sites aboved used as reference.

class ssocket:
    def __init__(self, blah):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.msg = ""

    def connect(self, host, port):
        self.sock.connect((host, port))
        self.connected = True

    def setupServer(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen()
        self.connected = True
        self.mreceive()


    def msend(self, msg):
        self.sock.sendall(str.encode(msg))

    def mreceive(self):
            conn, addr = self.sock.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
                    print('Message Received: ' + str(data))
