from Protocol import Protocol
from Client import Client

import pathlib
import sys
import os
import re

class CLI():
# """
# Commmand Line Interfaceused to initalize a P2P network
# Currently implemented: Initialize, Start Network and Connect to Network
# """
    def __init__(self):
        print("------------------------------------------------")
        print("SourceConnect")
        print("A collaborative terminal based directory!")
        print("------------------------------------------------")

        print("to begin, please specify the path of the")
        print("directory you would like to share (It is best")
        print("if this is an empty directory on your computer)")



        self.shared_dir = self.get_usr_directory()
        self.listening_addr = self.get_usr_ip_and_port()
        self.init_dir()

        self.join_or_create_network()

        while (1):
            self.list_or_req()

    def get_usr_directory(self):
        is_valid_path = False

        while (not is_valid_path):
            print()
            sys.stdout.write('directory path: ')
            sys.stdout.flush()
            usr_selection = input()
            usr_path = pathlib.Path(usr_selection)
            print()

            if (not usr_path.exists()):
                print("<<ERROR: path does not exist>>")

            elif (not usr_path.is_dir()):
                print("<<ERROR: path is not a directory>>")

            else:
                is_valid_path = True
                print()
                return usr_path

    def get_usr_ip_and_port(self):
        print("please provide an addressthat others can use")
        print("to access your directory in the form ip:port")
        print()

        return self.get_addr()


    def join_or_create_network(self):
        print("would you like to join an existing network or would")
        print("you like to create your own?")

        print("1: create a netork || 2: join a network")

        is_valid_input = False
        while (not is_valid_input):
            print()
            sys.stdout.write('(1 or 2): ')
            sys.stdout.flush()
            usr_input = input()
            print()


            if (usr_input != "1" and usr_input != "2"):
                print("<<ERROR: input out of range>>")

            else:
                if (usr_input == "1"):
                    print("creating a new network...")
                    print()
                    self.handle_start_network()

                elif (usr_input == "2"):
                    print("please provide address of a node in the netowrk")
                    print("in the form ip:port")
                    print()
                    new_node_addr = self.get_addr()
                    self.handle_join_network(new_node_addr)

                is_valid_input = True



    def get_addr(self):
        is_valid_addr = False
        while (not is_valid_addr):
            sys.stdout.write('addr: ')
            sys.stdout.flush()
            usr_input = input()

            ip_port_re = r"(\d+\.\d+\.\d+\.\d+):(\d+)"

            match = re.match(ip_port_re, usr_input)
            if (not match):
                print("<<ERROR: not a valid addr in form ip:port>>")

            else:
                listen_addr = (match.group(1), int(match.group(2)))
                is_valid_addr = True
                print()
                return listen_addr

    def list_or_req(self):
        print()
        print("1: list available files  || 2: request a file")

        is_valid_input = False
        while (not is_valid_input):
            print()
            sys.stdout.write('(1 or 2): ')
            sys.stdout.flush()
            usr_input = input()
            print()


            if (usr_input != "1" and usr_input != "2"):
                print("<<ERROR: input out of range>>")

            else:
                if (usr_input == "1"):
                    print("connecting to nodes for file list...")
                    print()
                    self.client_obj.list_files()

                elif (usr_input == "2"):
                    print()
                    print("please provide the name of a file to request")
                    print()

                    sys.stdout.write('filename: ')
                    sys.stdout.flush()

                    req_file_name = input()
                    self.client_obj.request_file(req_file_name)

                is_valid_input = True





    def init_dir(self):
        addrs_file_path = self.shared_dir.joinpath(".addrs.config")

        if addrs_file_path.exists():
            addrs_file_path.unlink()

        with open(self.shared_dir.joinpath(".addrs.config"), "w") as addrs_file:
            file_content = "0: " + self.listening_addr[0] + " " + str(self.listening_addr[1]) + "\n"
            addrs_file.write(file_content)


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
        self.client_obj = Client(self.shared_dir, self.listening_addr)
        self.client_obj.start_listening_thread()


    def handle_join_network(self, connection_addr):
        # """Connects two nodes in the network to eachother
        # @params: shared directory, connection ip and connection port"""
        #cli connenct_to_network shared_dir conn_ip, conn_port

        connection_addr =  connection_addr

        self.client_obj = Client(self.shared_dir, self.listening_addr)
        self.client_obj.start_listening_thread()

        self.client_obj.join_network(connection_addr)


if __name__ == "__main__":
    cl = CLI()
