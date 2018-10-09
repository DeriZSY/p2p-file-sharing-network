import time

def server_listening(server_addr):
    print(time.asctime(time.localtime()))
    print("<<SERVER LISTENING>>")
    print("server addr: " + str(server_addr))
    print()

def server_new_connection(client_addr):
    print(time.asctime(time.localtime()))
    print("<<NEW CONNECTION TO SERVER>>")
    print("client addr: " + str(client_addr))
    print()

def server_connection_closed(client_addr):
    print(time.asctime(time.localtime()))
    print("<<CONNECTION TO THE SERVER CLOSED>>")
    print("client_addr: " + str(client_addr))
    print()

def server_new_message(message, client_addr):
    print(time.asctime(time.localtime()))
    print("<<SERVER RECIEVED DATA>>")
    print("client_addr: " + str(client_addr))
    print("data: " + message)
    print()



def client_new_message(message, client_addr):
    print(time.asctime(time.localtime()))
    print("<<Client RECIEVED DATA>>")
    print("client_addr: " + str(client_addr))
    print("data: " + message)
    print()
