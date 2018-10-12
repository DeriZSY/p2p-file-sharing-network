from Protocol import Protocol
from threading import Thread
import socket
import time

# peer handle thread always starts by sending a message. any recieving should be done elsehwere
class PeerHandleThread(Thread):
    def __init__(self, audit, parent_client, client_sock, recipient_addr, message_type):
        Thread.__init__(self)
        self.audit = audit

        self.client_sock = client_sock
        self.recipient_addr = recipient_addr

        self.message_type = message_type

    def run(self):
        # self.client_sock.connect(self.recipient_addr)

        if self.message_type == Protocol.ping_to_string():
            self.handle_ping()

        elif self.message_type == Protocol.pong_to_string():
            self.handle_pong()

        elif self.message_type == Protocol.req_file_string():
            self.handle_req_file()

        elif self.message_type == Protocol.send_file_string():
            self.handle_send_file()

    def handle_req_file(self):
        self.audit.sending_data(Protocol.req_file_bytes())
        self.client_sock.sendall(Protocol.req_file_bytes())

        while (1):
            data = self.client_sock.recv(8)

            if not data:
                print("connection closed")
                break

            data = data.decode("UTF-8")
            self.audit.data_recieved(data)

    def handle_send_file(self):
        self.audit.sending_data(Protocol.send_file_bytes())
        self.client_sock.sendall(Protocol.send_file_bytes())

        while (1):
            data = self.client_sock.recv(8)

            if not data:
                print("connection closed")
                break

            data = data.decode("UTF-8")
            self.audit.data_recieved(data)




    def handle_ping(self):
        self.audit.sending_data(Protocol.ping_to_bytes())
        self.client_sock.sendall(Protocol.ping_to_bytes())

        while (1):
            data = self.client_sock.recv(8)

            if not data:
                print("connection closed")
                break

            data = data.decode("UTF-8")
            self.audit.data_recieved(data)

            if data == Protocol.pong_to_string():
                time.sleep(1)
                self.client_sock.sendall(Protocol.ping_to_bytes())
            else:
                print("its broke!")
                break

    def handle_pong(self):
        self.audit.sending_data(Protocol.pong_to_bytes())
        self.client_sock.sendall(Protocol.pong_to_bytes())

        while (1):
            data = self.client_sock.recv(8)

            if not data:
                print("connection closed")
                break

            data = data.decode("UTF-8")
            self.audit.data_recieved(data)

            if data == Protocol.ping_to_string():
                self.client_sock.sendall(Protocol.pong_to_bytes())
            else:
                print("its broke!")
                break
