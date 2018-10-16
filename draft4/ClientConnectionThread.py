import uuid
from Utils import FileReader
from Utils import DirectoryReader
from Protocol import Protocol
from threading import Thread
import socket
import os

class ClientConnectionThread(Thread):
    # """Utilizes TCP to initialize a thread for every peer connection in the network"""
    def __init__(self, shared_dir_path, client_connection):
        Thread.__init__(self)
        self.shared_dir_path = shared_dir_path
        self.client_connection = client_connection

    def run(self):
        while (1):
            data = self.client_connection.recv(8)

            if not data:
                print("The connection was closed")
                break

            data_str = data.decode("UTF-8")

            print("Data recieved")
            print(data_str)
            print()

            if data_str == Protocol.req_join_string():
                self.handle_join_network_request()

            elif data_str == Protocol.ack_join_string():
                self.handle_ack_join_network_request()

            if data_str == Protocol.req_list_string():
                self.handle_list_request()

            elif data_str == Protocol.ack_list_string():
                self.handle_ack_list_request()

    def handle_join_network_request(self):
        f = FileReader(self.shared_dir_path + "/addrs.config")
        addrs_bytes = f.get_file_bytes()

        self.client_connection.sendall(Protocol.ack_join_bytes(addrs_bytes))

    def handle_ack_join_network_request(self):
            file_size_bytes = self.client_connection.recv(8)
            byte_length = Protocol.fixed_width_bytes_to_int(file_size_bytes)

            file_bytes = self.client_connection.recv(byte_length)

            with open(os.path.join(self.shared_dir_path + "/tmp"), 'wb') as temp_file:
                temp_file.write(file_bytes)

            sender_addr = Protocol.parse_config_file(self.shared_dir_path + "/tmp")["0"]

            with open(os.path.join(self.shared_dir_path + "addrs.config"), 'ab') as addrs_file:
                addrs_file.write(str(uuid.uuid1()).encode("UTF-8"))
                addrs_file.write(b": ")
                addrs_file.write(sender_addr[0].encode("UTF-8"))
                addrs_file.write(b" ")
                addrs_file.write(str(sender_addr[1]).encode("UTF-8"))
                addrs_file.write(b"\n")

            if os.path.isfile(self.shared_dir_path + "/tmp"):
                os.remove(self.shared_dir_path + "/tmp")

    def handle_list_request(self):
        file_list = DirectoryReader(self.shared_dir_path).list_file_names()
        self.client_connection.sendall(Protocol.ack_list_bytes(file_list))

    def handle_ack_list_request(self):
        list_size_bytes = self.client_connection.recv(8)
        list_bytes = self.client_connection.recv(Protocol.fixed_width_bytes_to_int(list_size_bytes))
        list_str = list_bytes.decode("UTF-8")
        file_name_list = list_str.split("\n")
        print(file_name_list)
