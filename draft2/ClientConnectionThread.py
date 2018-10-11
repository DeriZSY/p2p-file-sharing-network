from threading import Thread
import socket

class ClientConnectionThread(Thread):
    def __init__(self, ingress_parent, connection_socket):
        Thread.__init__(self)

        self.ingress_parent = ingress_parent
        self.connection_socket = connection_socket

    def run(self):
        while (1):
            incoming_data = self.connection_socket.recv(8)

            if not incoming_data:
                self.connection_socket.close()
                break

            # todo deal with different incoming messages here
            print("ingress client recieved data: " + incoming_data.decode("UTF-8"))
