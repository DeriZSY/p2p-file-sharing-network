# TODO: add a line of code that will give the new threads to the calling parents
from PeerHandleThread import PeerHandleThread
import socket
from Protocol import Protocol
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
            self.audit.new_connection(new_conn_addr)
            self.recieve_data(new_conn_sock, new_conn_addr)




    def recieve_data(self, new_conn_sock, new_conn_addr):
        while (1):
            data = new_conn_sock.recv(32)

            if not data:
                self.audit.connection_closed(self.listening_addr, new_conn_addr)
                break

            self.audit.data_recieved(data)
            data = data.decode("UTF-8")

            if data == Protocol.ping_to_string():
                pt = PeerHandleThread(self.audit, self.parent_client, new_conn_sock, new_conn_addr, Protocol.pong_to_string())
                pt.start()
