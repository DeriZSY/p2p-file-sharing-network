from threading import Thread
import socket

class ClientIngressThread(Thread):
    def __init__(self, calling_client, client_ip, client_port):
        Thread.__init__(self)

        self.calling_client = calling_client
        self.calling_client_addr = (client_ip, client_port)

        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.bind(self.calling_client)


    def run(self):
        self.
