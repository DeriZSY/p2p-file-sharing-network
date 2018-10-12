import sys
import socket
from threading import Thread

class Peer:
"""Implements the basic functionality of a P2P network"""

    def __init__(self, maxPeers, serverPort, myId = None, serverHost = None):
        self.maxpeers = int(maxPeers)
        self.serverPort = int(serverPort)

        #Except IP connection to a serverHost if none provided
        if serverhost != None:
            self.serverHost = serverHost
        else:
            self.__initserverhost()

        #Except a Peer Id in case one isn't provided
        if myId != None:
            self.myId = myId
        else:
            self.myId = '%s:%d' % (self.serverHost. self.serverPort)

        #Keeps a dictionary of all the peers it might connect to
        self.peers = {}


        self.handlers = {}

        #Parametrically undeclared variables.
        self.router = None
        self.debug = 0
        self.shutdown = False

    def main():
        #TODO: #make a socket that the peer can connet #
        while(True):
            clientSock, clientAddress = s.accept()

            thread = threading.Thread()
