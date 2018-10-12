# TODO: send a message
# TODO: send a message of variable length

from PeerHandleThread import PeerHandleThread
from MainLoopThread import MainLoopThread
from Protocol import Protocol
import socket

class Peer():
    def __init__(self, audit, listening_addr):
        self.audit = audit
        self.listening_addr = listening_addr

        self.ingress_connection_threads = []
        self.start_main_loop_listening()


    def start_main_loop_listening(self):
        self.main_loop_thread = MainLoopThread(self.audit, self, self.listening_addr)
        self.main_loop_thread.start()

    def send_message(self, recipient_addr):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        c2c = PeerHandleThread(self.audit, self, client_sock, recipient_addr)
        c2c.start()

    def send_ping(self, recipient_addr):
        message_type = Protocol.ping_to_string()

        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(recipient_addr)

        c2c = PeerHandleThread(self.audit, self, client_sock, recipient_addr, message_type)

        c2c.start()
