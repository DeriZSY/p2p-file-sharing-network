import socket


class Server():

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_port.bind((self.server_ip, self.server_port))

    def main(self):
        


if __name__ == "__main__":
    s = Server(sys.argv[1], int(sys.argv[2]))
