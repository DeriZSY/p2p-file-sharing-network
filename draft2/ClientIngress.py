from ClientConnectionThread import ClientConnectionThread
from threading import Thread
import socket

class ClientIngress(Thread):
    def __init__(self, parent_client, parent_addr):
        Thread.__init__(self)
        self.ingress_threads = []

        self.parent_client = parent_client
        self.parent_client_addr = parent_addr

        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.bind(self.parent_client_addr)


    def run(self):
        self.listening_socket.listen()

        while (1):
            conn_socket, conn_addr = self.listening_socket.accept()

            connection_thread = ClientConnectionThread()
            connection_thread.start()

            self.remove_stale_ingress_threads()
            self.ingress_threads.append(connection_thread)


    def remove_stale_ingress_threads(self):
        self.ingress_threads = [conn for conn in self.ingress_threads if conn.is_alive()]
