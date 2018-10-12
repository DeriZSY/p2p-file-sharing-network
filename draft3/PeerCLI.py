from Audit import Audit
from Peer import Peer
import sys
import re
import time


class PeerCLI():
    def __init__(self, config_file_path, listening_addr_key, recieving_addr_key):
        self.audit = Audit()

        self.config_addrs = self.parse_config_file(config_file_path)
        self.listening_addr = self.config_addrs[listening_addr_key]
        self.recieving_addr = self.config_addrs[recieving_addr_key]

        self.peer = Peer(self.audit, self.listening_addr)
        self.send_message_prompt()

    def send_message_prompt(self):
        time.sleep(1/100)
        
        send_ping = sys.argv[4]

        if send_ping == "y":
            self.peer.send_ping(self.recieving_addr)


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
    cd = PeerCLI(sys.argv[1], sys.argv[2], sys.argv[3])
