import socket
import time
import sys
import audit
from P2PRequests import request_file_message

class Client():

    def __init__(self, file_name_req, server_ip, server_port):
        self.file_name_req = file_name_req

        self.server_ip = server_ip
        self.server_port = server_port
        self.server_addr = (self.server_ip, self.server_port)

        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.connect(self.server_addr)

        self.main()

    def main(self):
        while (1):
            self.request_file()
            self.recieve_response()

    def request_file(self):
        time.sleep(.5)
        self.server_sock.sendall(request_file_message(self.file_name))

    def recieve_response(self):
        data = self.server_sock.recv(16)

        if not data:
            print("the server closed the connection")
            sys.exit(1)

        message = data.decode("ascii")
        audit.client_new_message(message, self.server_addr)



    def recieve_header(self):
        data = self.server_sock.recv(8)

        if not data:
            print("the server closed the connection")
            sys.exit(1)

        message = data.decode("UTF-8")

        if (message == "FNF     "):
            print("ther server aint got that file")

        elif (message == "ACK     "):
            print("recieving file")
            file_size = self.recieve_file_size()
            self.recieve_file(file_size)

    def recieve_file(self, file_size):
        data = self.server_sock.recv(file_size)

        if not data:
            print("the server closed the connection")
            sys.exit(1)

        print(data.decode("UTF-8"))
        return file_size


    def recieve_file_size(self):
        data = self.server_sock.recv(8)

        if not data:
            print("the server closed the connection")
            sys.exit(1)

        file_size = int.from_bytes(data, "big")
        return file_size


if __name__ == "__main__":
    c = Client(sys.argv[1], sys.argv[2], int(sys.argv[3]))
