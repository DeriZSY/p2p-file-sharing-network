from Peer import debugOut

## Peer.py adapted from cs.berry.edu's btpeer.py

class PeerConnection:

    def __debug(self, message):
        if self.debug:
            debugOut(message)

    def __init__ (self, peerID, host, port, Socket=None, debug=False):
        self.id = peerID
        self.debug = debug

    if not sock:
        self.socket = socket.socket(SOCK_STREAM)
        self.socket.connect((host, int(port)))
    else:
        self.socket = Socket

    #random variables
    self.sd = self.socket.makefile('rw', 0)

    def createMessage(self, messageType, messageData):
        messageLength = len(messageData)
        #TODO: Unsure about this weird regex, I;d probably be happier changing this.
        message = struct.pack("!4sL%ds" % messageLength, messageType, messageLength, messageData)
        return message

    def sendData(self, messageType, messageData):
    ## TODO: Javadoc for all these functions.
    try:
        message = self.createMessage(messageType, messageData)
        ## TODO: this both belong to the weird instance variable for this class.
        self.sd.write(message)
        self.sd.flush()

    except KeyboardInterrupt:
        raise

    except:
        ## TODO: figure out how to use debug for all these functions.
        if self.debug:
            pass

    def recvdata(self):
    ## TODO: refactor function to unpack the message chunks better.
    try:
        messageType = self.sd.read(4)
        if not messageType:
            return (None, None)

        lengthStr = self.sd.read(4)
        ## TODO: starting to think that this isn't regex.
        messageLength = int(struct.unpack("!L", lenstr)[0])
        message = ""

        while len(message) != messageLength:
            data = self.sd.read(min(2048, messageLength - len(message))
            if not len(data):
                break
            message += data

            if len(message) != messageLength:
                return (None, None)

        except KeyboardInterrupt:
            raise
        except:
            if self.debug:
                return (None, None)
            ## TODO: Isn't there a better way to throw all these exeptions into a function?
        return (messageType, message)

    def close(self):
        self.socket.close()
        self.socket = None
        self.sd = None

    def __str__(self):
        return "|%s|" % peerID
