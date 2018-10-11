import socket
from threading import Thread

class ClientToServerThread(Thread):

    def __init__(self, server_ip, server_port):
        Thread.__init__(self)
        self.server_addr = (server_ip, server_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        self.sock.connect(self.server_addr)
