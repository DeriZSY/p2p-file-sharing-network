from Protocol import Protocol
from Client import Client

import sys
import os
import re

class CLI():
# """
# Commmand Line Interfaceused to initalize a P2P network
# Currently implemented: Initialize, Start Network and Connect to Network
# """
    def __init__(self):
        if sys.argv[1] == "init":
            self.handle_init_dir()
            sys.exit(0)

        elif sys.argv[1] == "start_network":
            self.handle_start_network()

        elif sys.argv[1] == "connect_to_network":
            self.handle_conn_network()

        while (1):
            next_command = input()

            if next_command == "list":
                self.client_obj.list_files()

            elif next_command[:3] == "req":
                file_name = next_command[4:]
                self.client_obj.request_file(file_name)




    def handle_init_dir(self):
    # """Handles the creation of a meta file that contains information regarding the nodes in
    # the network currently part of the P2P network"""
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):

            # TODO: add check for writing in ip and port
            listening_ip = sys.argv[3]
            listening_port_str = sys.argv[4]

            if os.path.isfile(os.path.join(dir_path, "addrs.config")):
                os.remove(os.path.join(dir_path, "addrs.config"))

            with open(os.path.join(dir_path, "addrs.config"), 'wb') as temp_file:
                temp_file.write(b"0: ")
                temp_file.write(listening_ip.encode("UTF-8"))
                temp_file.write(b" ")
                temp_file.write(listening_port_str.encode("UTF-8"))
                temp_file.write(b"\n")

        else:
            print("<<ERROR: invalid shared_dir provided>>")


    def handle_start_network(self):
    # """Initializes a shared directory, enabling other peers to connect to a shared directory of files."""
        # cli start_network shared_dir
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):
            listneing_addr = Protocol.parse_config_file(os.path.join(dir_path, "addrs.config"))["0"]

            self.client_obj = Client(dir_path, listneing_addr)
            self.client_obj.start_listening_thread()

        else:
            print("<<ERROR: invalid shared_dir provided>>")


    def handle_conn_network(self):
        # """Connects two nodes in the network to eachother
        # @params: shared directory, connection ip and connection port"""
        #cli connenct_to_network shared_dir conn_ip, conn_port
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):
            conn_ip = sys.argv[3]
            conn_port_str = sys.argv[4]

            conn_addr = (conn_ip, int(conn_port_str))
            listneing_addr = Protocol.parse_config_file(os.path.join(dir_path, "addrs.config"))["0"]

            self.client_obj = Client(dir_path, listneing_addr)
            self.client_obj.start_listening_thread()

            self.client_obj.join_network(conn_addr)

        else:
            print("<<ERROR: invalid shared_dir provided>>")

if __name__ == "__main__":
    cl = CLI()
