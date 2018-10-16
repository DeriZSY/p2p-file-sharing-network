from ClientConnectionThread import ClientConnectionThread

import socket
from threading import Thread

class ListenThread(Thread):
    def __init__(self, parent_client, listening_addr):
        Thread.__init__(self)
        self.parent_client = parent_client
        self.listening_addr = listening_addr

        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.bind(self.listening_addr)


    def run(self):
        print("listening")
        self.listening_socket.listen()

        while (1):
            connection_socket, connection_addr = self.listening_socket.accept()
            new_client_connection_thread = ClientConnectionThread(connection_socket)
            new_client_connection_thread.start()

            self.parent_client.connections.append(new_client_connection_thread)
