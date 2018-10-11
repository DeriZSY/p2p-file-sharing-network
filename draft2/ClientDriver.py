from Client import Client
import sys


class ClientDriver():
    def __init__(self, function, my_addr, other_addr):
        if function == "s":
            self.client = Client(my_addr)
        elif function == "c":
            self.client = Client(my_addr)
            print("please enter a message to send:")
            message = input()
            self.client.send_message(message, other_addr)



if __name__ == "__main__":
    c = ClientDriver(sys.argv[1], (sys.argv[2], int(sys.argv[3])), (sys.argv[4], int(sys.argv[5])))
