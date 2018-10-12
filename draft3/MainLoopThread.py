# TODO: add a line of code that will give the new threads to the calling parents
import socket
from threading import Thread

class MainLoopThread(Thread):
    def __init__(self, audit, parent_client, listening_addr):
        Thread.__init__(self)
        self.audit = audit

        self.parent_client = parent_client

        self.listening_addr = listening_addr
        self.initialize_and_bind_socket()

    def initialize_and_bind_socket(self):
        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.bind(self.listening_addr)

    def run(self):
        self.listening_socket.listen()
        self.audit.ingress_listening(self.listening_addr)

        while (1):
            new_conn_sock, new_conn_addr = self.listening_socket.accept()
            PeerHandleThread(self, new_conn_sock)
            self.recieve_data(new_conn_sock, new_conn_addr)



    def recieve_data(self, new_conn_sock, new_conn_addr):
        while (1):
            data = new_conn_sock.recv(32)

            if not data:
                self.audit.connection_closed(self.listening_addr, new_conn_addr)
                break

            self.audit.data_recieved(self.listening_addr, new_conn_addr, data)
