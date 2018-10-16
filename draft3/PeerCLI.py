from Audit import Audit
from Peer import Peer
import sys
import re
import time
import os


class PeerCLI():
    def __init__(self, config_file_path, listening_addr_key, recieving_addr_key):
        self.audit = Audit()

        self.config_addrs = self.parse_config_file(config_file_path)
        self.listening_addr = self.config_addrs[listening_addr_key]
        self.recieving_addr = self.config_addrs[recieving_addr_key]

        self.peer = Peer(self.audit, self.listening_addr)
        self.do_something()

    def do_something(self):
        time.sleep(1/100)

        to_do_or_not_to_do = sys.argv[4]

        if to_do_or_not_to_do == "y":
            # self.peer.send_ping(self.recieving_addr)
            self.peer.request_file(self.recieving_addr)


    def parse_config_file(self, config_file_path):
        try:
            config_file = open(config_file_path)
            file_contents = config_file.read()
            regex = r"(\d):\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+)"

            match = re.search(regex, file_contents)
            if match:
                matches = re.findall(regex, file_contents)
                addrs = {a[0] : (a[1], int(a[2])) for a in matches}
                return addrs

            else:
                print("<<ERROR: invalid config file format>>")
                print("exiting...")
                sys.exit(1)

        except FileNotFoundError:
            print("<<ERROR: invalid config file path>>")
            print("exiting...")
            sys.exit(1)


if __name__ == "__main__":
    # init shared_dir 127.0.0.1 9090
    # inti shared_dir, listening_addr, port
    # This code takes a dir path and adds in your listening addr and port as the first entry
    if sys.argv[1] == "init_dir":
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):

            # TODO: add check for writing in ip and port
            listening_ip = sys.argv[3]
            listening_port_str = sys.argv[4]

            with open(os.path.join(dir_path, "addrs.config"), 'wb') as temp_file:
                temp_file.write(b"0: ")
                temp_file.write(listening_ip.encode("UTF-8"))
                temp_file.write(b" ")
                temp_file.write(listening_port_str.encode("UTF-8"))
                temp_file.write(b"\n")

        else:
            print("Really? is it so hard to just give me a directory???")

    # connect 127.0.01 9090
    # ip and port to connect to
    elif sys.argv[1] == "start":
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):

            # TODO: add check for writing in ip and port
            conn_ip = sys.argv[3]
            listening_port_str = sys.argv[4]

            with open(os.path.join(dir_path, "addrs.config"), 'wb') as temp_file:
                temp_file.write(b"0: ")
                temp_file.write(listening_ip.encode("UTF-8"))
                temp_file.write(b" ")
                temp_file.write(listening_port_str.encode("UTF-8"))
                temp_file.write(b"\n")

        else:
            print("Really? is it so hard to just give me a directory???")




    # # cd = PeerCLI(sys.argv[1], sys.argv[2], sys.argv[3])
