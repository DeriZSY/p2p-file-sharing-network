import os
import re
import sys

STR_LENGTH = 8
INT_LENGTH = 8

class Protocol():

    # -----------------------------------------------------------------------------------------------

    @classmethod
    def req_file_string(self, filename = None):
        if (filename):
            print("This will be added")
        return self.str_to_fixed_width_string("reqfile")

    @classmethod
    def req_file_bytes(self, filename = None):

        if (filename):
            file_name_bytes = filename.encode("UTF-8")
            filename_byte_len = len(file_name_bytes)
            return self.req_file_bytes() + self.int_to_fixed_width_bytes(filename_byte_len) + file_name_bytes

        return self.str_to_fixed_width_string("reqfile").encode("UTF-8")

    # -----------------------------------------------------------------------------------------------

    @classmethod
    def req_join_string(self):
        return self.str_to_fixed_width_string("reqjoin")

    @classmethod
    def req_join_bytes(self):
        return self.str_to_fixed_width_string("reqjoin").encode("UTF-8")

    # -----------------------------------------------------------------------------------------------

    @classmethod
    def ack_join_string(self):
        return self.str_to_fixed_width_string("ackjoin")

    @classmethod
    def ack_join_bytes(self, file_bytes = None):
        if (file_bytes):
            file_byte_len = len(file_bytes)
            return self.ack_join_bytes() + self.int_to_fixed_width_bytes(file_byte_len) + file_bytes

        return self.str_to_fixed_width_string("ackjoin").encode("UTF-8")


    # -----------------------------------------------------------------------------------------------


    @classmethod
    def req_list_string(self):
        return self.str_to_fixed_width_string("reqlist")

    @classmethod
    def req_list_bytes(self):
        return self.str_to_fixed_width_string("reqlist").encode("UTF-8")

    # -----------------------------------------------------------------------------------------------


    @classmethod
    def ack_list_string(self):
        return self.str_to_fixed_width_string("acklist")

    @classmethod
    def ack_list_bytes(self, file_list = None):
        if (file_list):

            file_list_str = "\n".join(file_list)
            file_list_bytes = file_list_str.encode("UTF-8")
            file_list_byte_len = len(file_list_bytes)

            return self.ack_list_bytes() + self.int_to_fixed_width_bytes(file_list_byte_len) + file_list_bytes

        return self.str_to_fixed_width_string("acklist").encode("UTF-8")

    # -----------------------------------------------------------------------------------------------

    @classmethod
    def str_to_fixed_width_string(self, _str):
        str_len = len(_str)

        output_str = _str
        for i in range(0, STR_LENGTH - str_len):
            output_str += " "

        return output_str

    # -----------------------------------------------------------------------------------------------

    @classmethod
    def int_to_fixed_width_bytes(self, _int):
        return (_int).to_bytes(8, "big")

    @classmethod
    def fixed_width_bytes_to_int(self, _bytes):
        return int.from_bytes(_bytes, "big")


    # -----------------------------------------------------------------------------------------------
    @classmethod
    def parse_config_file(self, config_file_path):
        # """ Gathers information from a network metafile, utilizes regex to verify a valid IP is given
        # then creates a dictionary that matches directories with the respective IP adresses."""
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
            print("<<ERROR: no config file found>>")
            print("please reinitialize your shared_dir")
            print("exiting...")
            sys.exit(1)
