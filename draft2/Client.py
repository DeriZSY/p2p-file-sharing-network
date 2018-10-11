from ClientIngress import ClientIngress
from ClientEgress import ClientEgress
import socket
import sys

class Client():

    def __init__(self, listening_addr):
        self.listening_addr = listening_addr

        self.start_ingress()



    def start_ingress(self):
        self.ingress = ClientIngress(self, self.listening_addr)
        self.ingress.start()

    def send_message(self, message, recipient_addr):
        e = ClientEgress(self, recipient_addr, message)





    #
    # def connect_to_server(self, server_ip, server_port):
    #     self.
    #
    # def connect_to_client(self):
    #     self.
