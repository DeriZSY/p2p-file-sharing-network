import Audit
from threading import Thread
import socket

class ClientToClientThread(Thread):
    def __init__(self, recipient_addr):
        Thread.__init__(self)
        self.recipient_addr = recipient_addr
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        print("message to send: ")
        message = input()
        message_bytes = message.encode("UTF-8")

        self.client_sock.connect(self.recipient_addr)
        Audit.sending_data(self.recipient_addr, message_bytes)
        self.client_sock.sendall(message_bytes)
