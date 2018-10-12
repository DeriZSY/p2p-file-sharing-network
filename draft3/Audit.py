from threading import Lock

class Audit():
    def __init__(self):
        self.io_lock = Lock()

    def bracket_text(self, text):
        return "<<" + text.upper() + ">>"

    def ingress_listening(self, listening_addr):
        self.io_lock.acquire()
        print(self.bracket_text("ingress listening"))
        print("listening at: " + str(listening_addr))
        print()
        self.io_lock.release()

    def connection_closed(self, host_addr, closing_addr):
        self.io_lock.acquire()
        print(self.bracket_text("connection_closed"))
        print("connection to: " + str(host_addr))
        print("closed by: " + str(closing_addr))
        print()
        self.io_lock.release()


    def data_recieved(self, host_addr, sending_addr, data):
        self.io_lock.acquire()
        print(self.bracket_text("data recieved"))
        print("sent from: "+ str(sending_addr))
        print("recieved by: "+ str(host_addr))
        print("data: "+ data.decode("UTF-8"))
        print()
        self.io_lock.release()

    def sending_data(self, recipient_addr, data):
        self.io_lock.acquire()
        print(self.bracket_text("seding data"))
        print("sent to: "+ str(recipient_addr))
        print("data sent: " + data.decode("UTF-8"))
        print()
        self.io_lock.release()

    def aprint(self, _str):
        self.io_lock.acquire()
        print(_str)
        self.io_lock.release()
