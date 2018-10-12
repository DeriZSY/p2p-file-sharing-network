# TODO: send a message
# TODO: send a message of variable length

from ClientToClientThread import ClientToClientThread
from ClientIngressThread import ClientIngressThread

class Client():
    def __init__(self, audit, listening_addr):
        self.audit = audit
        self.listening_addr = listening_addr

        self.ingress_connection_threads = []
        self.start_ingress_listening()


    def start_ingress_listening(self):
        self.ingress_thread = ClientIngressThread(self.audit, self, self.listening_addr)
        self.ingress_thread.start()

    def send_message(self, recipient_addr):
        c2c = ClientToClientThread(self.audit, recipient_addr)
        c2c.start()
