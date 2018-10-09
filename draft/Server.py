from pathlib import Path
import socket
import audit
import sys


class Server():

    def __init__(self, file_dir, server_ip, server_port):
        self.file_dir = Path(file_dir)

        self.server_ip = server_ip
        self.server_port = server_port

        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((self.server_ip, self.server_port))

        self.main()

    def main(self):
        self.server_sock.listen()
        audit.server_listening((self.server_ip, self.server_port))

        client_sock, client_addr = self.server_sock.accept()

        self.recv_messages(client_sock, client_addr)
        audit.server_new_connection(client_addr)

    def recv_messages(self, client_sock, client_addr):
        while (1):
            data = client_sock.recv(32)
            if not data:
                audit.server_connection_closed(client_addr)
                sys.exit(1)

            message = data.decode("ascii")
            audit.server_new_message(message, client_addr)

            self.ifPingSendPong(message, client_sock)

    def ifPingSendPong(self, message, client_sock):
        if message == "PING":
            client_sock.sendall(b"PONG")


if __name__ == "__main__":
    s = Server(sys.argv[1], sys.argv[2], int(sys.argv[3]))
