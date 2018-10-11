import sys
import re


class ClientDriver():
    def __init__(self, config_file_path, listening_addr_key, sending_addr_key):
        self.config_addrs = self.parse_config_file(config_file_path)
        self.listening_addr = self.config_addrs[listening_addr_key]
        self.sending_addr = self.config_addrs[sending_addr_key]

        print("listening_addr: " + str(self.listening_addr))
        print("sending_addr: " + str(self.sending_addr))


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
    cd = ClientDriver(sys.argv[1], sys.argv[2], sys.argv[3])
