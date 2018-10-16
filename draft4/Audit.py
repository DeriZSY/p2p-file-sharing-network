from threading import Lock

class Audit():
    def __init__(self):
        self.t = "t"
        # self.io_lock = Lock()


    def bracket_text(self, text):
        return "<<" + text.upper() + ">>"

    def ingress_listening(self, listening_addr):
        # self.io_lock.acquire()
        print(self.bracket_text("ingress listening"))
        print("listening at: " + str(listening_addr))
        print()
        # self.io_lock.release()

    def connection_closed(self, host_addr, closing_addr):
        # self.io_lock.acquire()
        print(self.bracket_text("connection_closed"))
        print("connection to: " + str(host_addr))
        print("closed by: " + str(closing_addr))
        print()
        # self.io_lock.release()


    def data_recieved(self, data):
        # self.io_lock.acquire()
        print(self.bracket_text("data recieved"))

        if (type(data) == str):
            print("data recieved: " + data)
        else:
            print("data recieved: " + data.decode("UTF-8"))

        print()
        # self.io_lock.release()

    def sending_data(self, data):
        # self.io_lock.acquire()
        print(self.bracket_text("data sent"))

        if (type(data) == str):
            print("data sent: " + data)
        else:
            print("data sent: " + data.decode("UTF-8"))

        print()
        # self.io_lock.release()

    def aprint(self, _str):
        # self.io_lock.acquire()
        print(_str)
        # self.io_lock.release()

    def new_connection(self, connection_addr):
        # self.io_lock.acquire()
        print(self.bracket_text("new connection"))
        print("connecting_addr: " + str(connection_addr))
        print()
        # self.io_lock.release()
