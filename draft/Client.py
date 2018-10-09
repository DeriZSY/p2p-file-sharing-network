import socket
import time
import sys

class Client():

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.connect((self.server_ip, self.server_port))

        self.main()

    def main(self):
        while (1):
            self.send_ping()
            self.recieve_response()

    def send_ping(self):
        time.sleep(.5)
        self.server_sock.sendall("hello world!")

    def recieve_response(self):
        data = self.server_sock.recv(16):

        if not data:
            print("the server closed the connection")
            sys.exit(1)

        print(data.decode("ascii"))


if __name__ == "__main__":
    c = Client(sys.argv[1], int(sys.argv[2]))
