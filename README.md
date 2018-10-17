# p2p-file-sharing-network
A peer to peer file sharing network that implements a protocol similar to the bitTorrent network.

## Running the file sharing service
In order to run this code, one only needs to navigate to the src directory and run the command `python3 CLI.py`.
This will start the command line interface for the software.

The program will prompt for users to enter the path for the directory they wish to initialize their shared directory in.
The user may enter an *absolute or relative path* for this prompt.

Once the program initializes, any files can be added to the users shared folder and they will be added to the network.
