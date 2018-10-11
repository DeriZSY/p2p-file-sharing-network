from pathlib import Path
import socket
import audit
import sys


class Server():

    def __init__(self, shared_files_dir, server_ip, server_port):
        self.shared_files_dir = shared_files_dir
        self.shared_file_paths = [f for f in self.shared_files_dir.iterdir()]

        self.server_ip = server_ip
        self.server_port = server_port

        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((self.server_ip, self.server_port))

        self.main()

    def main(self):
        self.server_sock.listen()
        audit.server_listening((self.server_ip, self.server_port))

        client_sock, client_addr = self.server_sock.accept()

        audit.server_new_connection(client_addr)
        self.recv_messages(client_sock, client_addr)

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
    try:
        shared_files_dir = Path(sys.argv[1])
        assert(shared_files_dir.is_dir())
    except AssertionError as e:
        print("Invalid path: Please provide a valide path name as the first argument")
        sys.exit(1)

    # Todo: add in a valid ip and valid port check here.

    s = Server(shared_files_dir, sys.argv[2], int(sys.argv[3]))
