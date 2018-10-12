from socket import socket, SOCK_DGRAM, SOCK_STREAM, timeout, AF_INET
from threading import Thread
from PeerConnection import PeerConnection
import sys
import re
import time, datetime

def debugOut( message ):
""" Prints a messsage to the screen with the name of the current thread """
print "[%s] %s" % ( str(threading.currentThread().getName()), msg )


class Peer:
"""Implements the basic functionality of a P2P network, attempting a decentralized architecture"""

    def __debug(self, message):
        if self.debug:
            debugOut(message)

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
        socket = self.makeSocketInstance(self.serverPort)
        socket.settimeout(2)
        #this line can totally make everything break
        self.__debug('Server started:' + str(self.myId) + " " + str(self.serverHost) +":" + str(self.serverPort))

        while (self.shutdown == False):
            try:
                self.__debug("Listening for connections...")
                clientSock, clientAddr = socket.accept()
                clientsock.settimeout(None)

            clientThread = threading.Thread( target = self.handlePeer, args = [ clientSock ])
            clientThread.start()

        except KeyboardInterrupt:
            self.shutdown = True
            continue
        except:
            #TODO: Some debug stuff i can't understand rn.
            pass

            self.__debug("Main loop terminating")
        socket.close()

    def handlePeer(self, clientSock):
        #TODO: What on earth is clientSock.getpeername
        self.__debug("Connected " + str(clientSock.getpeername()))

        host, port = clientsock.getpeername()
        peerConnection = PeerConnection(none, host, port, clientSock, debug=False)

        try:
            messageType, messageData = peerConnection.recvdata()
            if messageType:
                #TODO: guessing this simply makes the message upper case
                messageType = messageType.upper()

            if messageType not in self.handlers:
                self.__debug("Not handled: %s: %s" %(messageType, messageData))
            else:
                self.__debug('Handling peer msg %s: %s' %(messageType, messageData))
                self.handlers[messageType](peerConnection, messageData)

        except KeyboardInterrupt:
            raise

        except:
            #TODO: some traceback debug message

            self.__debug ('Disconnecting ' + str(clientSock.getpeername()))
            peerConnection.close()

    def makeSocketInstance(self, port):
        '''Makes a socket that can be reused when the OS closes the current thread'''
        socket = socket(SOCK_STREAM)
        socket.setsockopt(socket.SQL_SOCKET, SOCKET.SO_REUSEADDR, 1)
        socket.bind("", port)
        socket.listen(5)
    return socket
