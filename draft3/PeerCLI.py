from Audit import Audit
from Peer import Peer
import sys
import re
import time


class PeerCLI():
    def __init__(self, config_file_path, listening_addr_key):
        self.audit = Audit()

        self.config_addrs = self.parse_config_file(config_file_path)
        self.listening_addr = self.config_addrs[listening_addr_key]

        self.client = Peer(self.audit, self.listening_addr)
        self.send_message_prompt()

    def send_message_prompt(self):
        print("Send a message")
        invalid_addr = True
        while (invalid_addr):

            print("recipient_addr_key: ")
            recipient_addr_key = input()

            if (recipient_addr_key in self.config_addrs):
                invalid_addr = False

                self.client.send_message(self.config_addrs[recipient_addr_key])
            else:
                print("please enter a valid address key")



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
    cd = PeerCLI(sys.argv[1], sys.argv[2])
