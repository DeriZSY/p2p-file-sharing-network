from threading import Thread
import socket

class ClientConnectionThread(Thread):
    def __init__(self, client_connection):
        Thread.__init__(self)
        self.client_connection = client_connection

    def run(self):
        while (1):
            data = self.client_connection.recv(8)

            if not data:
                print("The connection was closed")
                break

            print("Data recieved")
            print(data.decode("UTF-8"))
