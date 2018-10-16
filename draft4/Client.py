from ClientConnectionThread import ClientConnectionThread
from ListenThread import ListenThread
import socket

class Client():
    def __init__(self, listening_addr):
        self.listening_addr = listening_addr
        self.connections = []

    def start_listening_thread(self):
        self.listening_thread = ListenThread(self, self.listening_addr)
        self.listening_thread.start()

    def join_network(self, connection_addr):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(connection_addr)

        client_socket.sendall(b"JOIN____")
        new_client_connection_thread = ClientConnectionThread(client_socket)
        new_client_connection_thread.start()
        self.connections.append(new_client_connection_thread)
