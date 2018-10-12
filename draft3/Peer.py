# TODO: send a message
# TODO: send a message of variable length

from PeerHandleThread import PeerHandleThread
from MainLoopThread import MainLoopThread

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
