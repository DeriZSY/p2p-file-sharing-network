# TODO: send a message
# TODO: send a message of variable length

from ClientToClientThread import ClientToClientThread
from ClientIngressThread import ClientIngressThread

class Client():
    def __init__(self, listening_addr):
        self.listening_addr = listening_addr

        self.ingress_connection_threads = []
        self.start_ingress_listening()


    def start_ingress_listening(self):
        self.ingress_thread = ClientIngressThread(self, self.listening_addr)
        self.ingress_thread.start()

    def send_message(self, recipient_addr):
        c2c = ClientToClientThread(recipient_addr)
        c2c.start()
