
from threading import Thread
import socket

class PeerHandleThread(Thread):
    def __init__(self, audit, parent_client, client_sock, recipient_addr):
        Thread.__init__(self)
        self.audit = audit

        self.client_sock = client_sock
        self.recipient_addr = recipient_addr

    def run(self):
        print("message to send: ")
        message = input()
        message_bytes = message.encode("UTF-8")

        self.client_sock.connect(self.recipient_addr)
        self.audit.sending_data(self.recipient_addr, message_bytes)
        self.client_sock.sendall(message_bytes)
