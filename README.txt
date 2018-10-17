Stream Connect File Sharing Network:
A peer to peer file sharing network that implements a protocol similar to
the bitTorrent network.

Downloading:
All of the code and history can be downloaded at the github link below:
https://github.com/bcarlborg/p2p-file-sharing-network.git

Running the file sharing service:
In order to run this code, one only needs to navigate to the src directory
and run the command `python3 CLI.py` where CLI.py is located in the src
directory. This will start the command line interface for the software.

The program will prompt for users to enter the path for the directory they
wish to initialize their shared directory in.
The user may enter an *absolute or relative path* for this prompt.

Once the program initializes, any files can be added to the users shared
folder and they will be added to the network.

Exiting the program preemptively will remove users from the network but
will not remove the files that the user has already downloaded using the system
