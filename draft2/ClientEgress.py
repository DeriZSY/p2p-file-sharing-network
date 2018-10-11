from ClientConnectionThread import ClientConnectionThread
from threading import Thread
import socket

class ClientEgress(Thread):

    def __init__(self, parent_client, recipient_addr, message):
        Thread.__init__(self)
        self.parent_client = parent_client
        self.recipient_addr = recipient_addr
        self.message = message

        self.egress_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def run(self):
        self.egress_sock.connect(self.recipient_addr)
        self.send_all(self.message.encode("UTF-8"))

        while (1):
            data = self.egress_sock.recv(8)
            if not data:
                print("connection closed")
                break;
            print("egress client recived data: " + data)
