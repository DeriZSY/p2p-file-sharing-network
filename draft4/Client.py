from Protocol import Protocol
from ClientConnectionThread import ClientConnectionThread
from ListenThread import ListenThread
import socket

class Client():
    def __init__(self, listening_addr):
    """Initates a peer node for a P2P network, takes in listening address"""
        self.listening_addr = listening_addr
        self.connections = []

    def start_listening_thread(self):
    """Initializes a thread for each of the connections that are added to the network"""
        self.listening_thread = ListenThread(self, self.listening_addr)
        self.listening_thread.start()

    def join_network(self, connection_addr):
    """Protocol utlized for each peer to join a network given one or more nodes initialized in
    P2P network."""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(connection_addr)

        client_socket.sendall(Protocol.req_join_bytes())

        new_client_connection_thread = ClientConnectionThread(client_socket)
        new_client_connection_thread.start()

        self.connections.append(new_client_connection_thread)
