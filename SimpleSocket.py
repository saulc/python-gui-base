import socket
# https://docs.python.org/3/howto/sockets.html
# https://realpython.com/python-sockets/
# echo server/client bare min for socet send/Received
# sites aboved used as reference.

class SimpleSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        else: self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def msend(self, msg):
        pass

    def mreceive(self):
        pass
