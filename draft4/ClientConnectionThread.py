from Protocol import Protocol
from threading import Thread
import socket

class ClientConnectionThread(Thread):
    """Utilizes TCP to initialize a thread for every peer connection in the network"""
    def __init__(self, client_connection):
        Thread.__init__(self)
        self.client_connection = client_connection

    def run(self):
        while (1):
            data = self.client_connection.recv(8)

            if not data:
                print("The connection was closed")
                break

            data_str = data.decode("UTF-8")

            print("Data recieved")
            print(data_str)

            if data_str == Protocol.req_join_string():
                self.handle_join_network_request()

            elif data_str == Protocol.ack_join_string():
                self.handle_ack_join_network_request()



    def handle_join_network_request(self):
        self.client_connection.sendall(Protocol.ack_join_bytes())

    def handle_ack_join_network_request(self):
        print("woohoo i'm in the club now!")
