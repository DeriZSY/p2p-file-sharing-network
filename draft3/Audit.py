def bracket_text(text):
    return "<<" + text.upper() + ">>"

def ingress_listening(listening_addr):
    print(bracket_text("ingress listening"))
    print("listening at: " + str(listening_addr))
    print()

def connection_closed(host_addr, closing_addr):
    print(bracket_text("connection_closed"))
    print("connection to: " + str(host_addr))
    print("closed by: " + str(closing_addr))
    print()


def data_recieved(host_addr, sending_addr, data):
    print(bracket_text("data recieved"))
    print("sent from: "+ str(sending_addr))
    print("recieved by: "+ str(host_addr))
    print("data: "+ data.decode("UTF-8"))
    print()

def sending_data(recipient_addr, data):
    print(bracket_text("seding data"))
    print("sent to: "+ str(recipient_addr))
    print("data sent: " + data.decode("UTF-8"))
    print()
