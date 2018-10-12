STR_LENGTH = 8
INT_LENGTH = 8

class Protocol():

    @classmethod
    def send_file_string(self, filename = None):
        if (filename):
            print("This will be added")
        return self.str_to_fixed_width_string("sendfile")

    @classmethod
    def send_file_bytes(self, filename = None):
        if (filename):
            print("This will be added")
        return self.str_to_fixed_width_string("sendfile").encode("UTF-8")


    @classmethod
    def req_file_string(self, filename = None):
        if (filename):
            print("This will be added")
        return self.str_to_fixed_width_string("reqfile")

    @classmethod
    def req_file_bytes(self, filename = None):
        if (filename):
            print("This will be added")
        return self.str_to_fixed_width_string("reqfile").encode("UTF-8")


    @classmethod
    def ping_to_bytes(self):
        return self.str_to_fixed_width_string("ping").encode("UTF-8")

    @classmethod
    def ping_to_string(self):
        return self.str_to_fixed_width_string("ping")

    @classmethod
    def ping_to_bytes(self):
        return self.str_to_fixed_width_string("ping").encode("UTF-8")

    @classmethod
    def ping_to_string(self):
        return self.str_to_fixed_width_string("ping")

    @classmethod
    def pong_to_bytes(self):
        return self.str_to_fixed_width_string("pong").encode("UTF-8")

    @classmethod
    def pong_to_string(self):
        return self.str_to_fixed_width_string("pong")

    @classmethod
    def str_to_fixed_width_string(self, _str):
        str_len = len(_str)

        output_str = _str
        for i in range(0, STR_LENGTH - str_len):
            output_str += " "

        return output_str
